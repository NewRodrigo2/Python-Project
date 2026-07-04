@echo off
:: Ajusta la ventana a 80 columnas de ancho y 25 líneas de alto
mode con: cols=80 lines=25

:: Ejecuta tu programa de Python
"%LOCALAPPDATA%\Programs\Python\Python313\python.exe" prueba.py

pause
