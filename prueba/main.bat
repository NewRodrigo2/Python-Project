@echo off
:: 1. Forzar a posicionarse en la carpeta del script .bat
cd /d "%~dp0"

:: 2. Ajustar el tamaño de la ventana
mode con: cols=100 lines=25

:: 3. VERIFICACIÓN INTELIGENTE DEL ENTORNO VIRTUAL
if exist ".venv\Scripts\python.exe" (
    set "PYTHON_PATH=.venv\Scripts\python.exe"
) else if exist "..\.venv\Scripts\python.exe" (
    set "PYTHON_PATH=..\.venv\Scripts\python.exe"
) else (
    :: Si no encuentra el entorno virtual, usará el Python de Windows por defecto
    set "PYTHON_PATH=python"
)

:: 4. EJECUTAR EL PROGRAMA
"%PYTHON_PATH%" main.py

pause
