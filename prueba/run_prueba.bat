@echo off
:: Ajusta la ventana a 80 columnas de ancho y 25 líneas de alto
mode con: cols=100 lines=25
:: color 8F

:: Ejecuta tu programa de Python
"%LOCALAPPDATA%\Programs\Python\Python313\python.exe" prueba.py

pause
