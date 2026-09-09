# ejemplo: mapa extendido con resumen funcional de métodos
import os, ast
from datetime import datetime

class MethodAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.calls = []
        self.self_attrs = []
        self.returns = []

    def visit_Call(self, node):
# Captura llamadas a funciones o métodos
        if isinstance(node.func, ast.Attribute):
            self.calls.append(ast.unparse(node.func))
        elif isinstance(node.func, ast.Name):
            self.calls.append(node.func.id)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        # Captura atributos self usados
        if isinstance(node.value, ast.Name) and node.value.id == "self":
            self.self_attrs.append(node.attr)
        self.generic_visit(node)

    def visit_Return(self, node):
        # Captura valores retornados
        if node.value:
            self.returns.append(ast.unparse(node.value))
        self.generic_visit(node)

class ClassAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.methods = []
        self.attrs = []
        self.bases = []

    def visit_FunctionDef(self, node):
        analyzer = MethodAnalyzer()
        analyzer.visit(node)
        self.methods.append({
            "name": node.name,
            "line": node.lineno,
            "calls": analyzer.calls,
            "self_attrs": analyzer.self_attrs,
            "returns": analyzer.returns
        })
        # Detectar asignaciones a self
        for stmt in node.body:
            if isinstance(stmt, ast.Assign):
                for target in stmt.targets:
                    if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                        asignacion = ast.unparse(stmt.value) if hasattr(ast, "unparse") else type(stmt.value).__name__
                        self.attrs.append((target.attr, stmt.lineno, asignacion))
        self.generic_visit(node)

def analizar_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=ruta)
    clases = {}
    for nodo in tree.body:
        if isinstance(nodo, ast.ClassDef):
            analyzer = ClassAnalyzer()
            analyzer.visit(nodo)
            bases = []
            for base in nodo.bases:
                bases.append(ast.unparse(base))
            analyzer.bases = bases
            clases[nodo.name] = {
                "methods": analyzer.methods,
                "attrs": analyzer.attrs,
                "bases": analyzer.bases
            }
    return clases

def analizar_proyecto(carpeta):
    mapa = {}
    for root, _, files in os.walk(carpeta):
        for file in files:
            if file.endswith(".py"):
                ruta = os.path.join(root, file)
                mapa[ruta] = analizar_archivo(ruta)
    return mapa

if __name__ == "__main__":

    #F:\Python\Python Project\prueba
    proyecto = analizar_proyecto("c:/Users/Rodrigo/Documents/GitHub/Python-Project/prueba")
    carpeta_mapas = os.path.join("c:/Users/Rodrigo/Documents/GitHub/Python-Project", "mapas")
    os.makedirs(carpeta_mapas, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_txt = os.path.join(carpeta_mapas, f"PROJECT_MAP_FUNC_{timestamp}.txt")

    with open(archivo_txt, "w", encoding="utf-8") as salida:
        salida.write(f"Mapa funcional del proyecto generado el {datetime.now()}\n")
        salida.write("="*60 + "\n")
        for archivo, clases in proyecto.items():
            salida.write(f"\nArchivo: {archivo}\n")
            for clase, info in clases.items():
                bases = ", ".join(info["bases"]) if info["bases"] else "object"
                salida.write(f"  Clase: {clase} (hereda de {bases})\n")
                salida.write("    Métodos:\n")
                for metodo in info["methods"]:
                    salida.write(f"      - {metodo['name']} (línea {metodo['line']})\n")
                    if metodo["calls"]:
                        salida.write(f"        Llama a: {', '.join(metodo['calls'])}\n")
                    if metodo["self_attrs"]:
                        salida.write(f"        Usa atributos: {', '.join(metodo['self_attrs'])}\n")
                    if metodo["returns"]:
                        salida.write(f"        Retorna: {', '.join(metodo['returns'])}\n")
                salida.write("    Atributos self:\n")
                for attr, linea, asignacion in info["attrs"]:
                    salida.write(f"      - self.{attr} = {asignacion} (línea {linea})\n")

    print(f"✅ Inventario funcional guardado en {archivo_txt}")
