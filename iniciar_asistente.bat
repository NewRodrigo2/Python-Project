@echo off
setlocal

cd /d "%~dp0"
if errorlevel 1 (
    echo No se pudo abrir la carpeta del proyecto.
    pause
    exit /b 1
)

start "Asistente local" powershell.exe -NoExit -Command "Set-Location -LiteralPath '%CD%'; python .\asistente_local.py"

endlocal
