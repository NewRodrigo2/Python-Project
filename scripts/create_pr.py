#!/usr/bin/env python3
"""
Script para crear un Pull Request en GitHub automáticamente.
Uso: python scripts/create_pr.py
"""

import requests
import json
import os
from pathlib import Path

# Configuración
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Debe estar en variables de entorno
REPO_OWNER = "NewRodrigo2"
REPO_NAME = "Python-Project"
HEAD_BRANCH = "class_python"  # Rama origen
BASE_BRANCH = "master"  # Rama destino

# URLs y Headers
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

def create_pull_request(title, body):
    """
    Crea un Pull Request en GitHub.
    
    Args:
        title (str): Título del PR
        body (str): Descripción del PR
    
    Returns:
        dict: Respuesta de la API con información del PR creado
    """
    payload = {
        "title": title,
        "body": body,
        "head": HEAD_BRANCH,
        "base": BASE_BRANCH,
    }
    
    print(f"\n📤 Creando Pull Request: '{title}'")
    print(f"   De: {HEAD_BRANCH} → A: {BASE_BRANCH}")
    print("-" * 60)
    
    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=10)
        
        if response.status_code == 201:
            pr_data = response.json()
            pr_number = pr_data["number"]
            pr_url = pr_data["html_url"]
            
            print(f"✅ ¡Pull Request creado exitosamente!")
            print(f"   PR #{pr_number}")
            print(f"   URL: {pr_url}")
            print("-" * 60)
            return pr_data
            
        elif response.status_code == 422:
            error = response.json()
            print(f"⚠️  Error 422 - Ya existe un PR abierto o error en los datos:")
            if "errors" in error:
                for err in error["errors"]:
                    print(f"   • {err.get('message', 'Error desconocido')}")
            print("-" * 60)
            return None
            
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            print("-" * 60)
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        print("-" * 60)
        return None

def validate_token():
    """Valida que el token de GitHub esté configurado."""
    if not GITHUB_TOKEN:
        print("\n❌ ERROR: Token de GitHub no configurado")
        print("\n📝 Para usar este script, necesitas:")
        print("   1. Crear un Personal Access Token en GitHub:")
        print("      - Ve a: https://github.com/settings/tokens")
        print("      - Crea un nuevo token con permisos 'repo'")
        print("\n   2. Configura la variable de entorno:")
        print("      • Windows (CMD): set GITHUB_TOKEN=tu_token_aqui")
        print("      • Windows (PowerShell): $env:GITHUB_TOKEN='tu_token_aqui'")
        print("      • Linux/Mac: export GITHUB_TOKEN=tu_token_aqui")
        print("\n   3. O crea un archivo .env en la raíz del proyecto:")
        print("      GITHUB_TOKEN=tu_token_aqui")
        print("-" * 60)
        return False
    return True

def main():
    """Función principal."""
    print("\n" + "="*60)
    print("🚀 SCRIPT PARA CREAR PULL REQUEST EN GITHUB")
    print("="*60)
    
    # Validar token
    if not validate_token():
        return
    
    # Solicitar información del usuario
    print("\n📋 Ingresa la información del Pull Request:")
    print("-" * 60)
    
    title = input("\n📌 Título del PR: ").strip()
    if not title:
        print("❌ El título no puede estar vacío")
        return
    
    print("\n📝 Descripción del PR (puedes escribir múltiples líneas)")
    print("   (Escribe 'FIN' en una línea nueva para terminar)")
    print("-" * 60)
    
    description_lines = []
    while True:
        line = input()
        if line.strip().upper() == "FIN":
            break
        description_lines.append(line)
    
    description = "\n".join(description_lines).strip()
    
    # Confirmar antes de crear
    print("\n" + "="*60)
    print("📋 RESUMEN DEL PR:")
    print("="*60)
    print(f"Título: {title}")
    print(f"Descripción:\n{description}")
    print(f"Rama origen: {HEAD_BRANCH}")
    print(f"Rama destino: {BASE_BRANCH}")
    print("="*60)
    
    confirm = input("\n¿Deseas crear este PR? (s/n): ").strip().lower()
    
    if confirm != "s":
        print("❌ Operación cancelada")
        return
    
    # Crear el PR
    create_pull_request(title, description)

if __name__ == "__main__":
    main()
