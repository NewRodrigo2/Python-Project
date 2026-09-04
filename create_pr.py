#!/usr/bin/env python3
"""
Script para crear automáticamente un Pull Request de class_python a master
Uso: GH_TOKEN=tu_token python create_pr.py
"""

import os
import sys
import requests
from datetime import datetime

# Configuración
REPO_OWNER = "NewRodrigo2"
REPO_NAME = "Python-Project"
BRANCH_SOURCE = "class_python"
BRANCH_TARGET = "master"
GH_API_URL = "https://api.github.com"

def get_token():
    """Obtener el token de GitHub desde variable de entorno"""
    token = os.getenv("GH_TOKEN")
    if not token:
        print("❌ Error: GH_TOKEN no está configurada")
        print("Usa: export GH_TOKEN='tu_token'")
        sys.exit(1)
    return token

def create_pull_request(token):
    """Crear un Pull Request"""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Datos del PR
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pr_data = {
        "title": f"Merge {BRANCH_SOURCE} to {BRANCH_TARGET}",
        "body": f"Automated PR created on {timestamp}\n\nMerging changes from `{BRANCH_SOURCE}` into `{BRANCH_TARGET}`",
        "head": BRANCH_SOURCE,
        "base": BRANCH_TARGET
    }
    
    # Endpoint para crear PR
    url = f"{GH_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    
    try:
        print(f"📝 Creando Pull Request de '{BRANCH_SOURCE}' a '{BRANCH_TARGET}'...")
        response = requests.post(url, json=pr_data, headers=headers)
        
        if response.status_code == 201:
            pr = response.json()
            print(f"✅ ¡PR creado exitosamente!")
            print(f"   PR #: {pr['number']}")
            print(f"   URL: {pr['html_url']}")
            return True
        
        elif response.status_code == 422:
            print("❌ Error: No hay cambios para mergear o el PR ya existe")
            print(f"   Respuesta: {response.json()}")
            return False
        
        elif response.status_code == 401:
            print("❌ Error: Token inválido o expirado")
            return False
        
        elif response.status_code == 403:
            print("❌ Error: Permisos insuficientes")
            return False
        
        else:
            print(f"❌ Error {response.status_code}: {response.json()}")
            return False
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return False

def main():
    """Función principal"""
    print(f"🔄 Script de Automatización de Pull Request")
    print(f"   Repositorio: {REPO_OWNER}/{REPO_NAME}")
    print(f"   Origen: {BRANCH_SOURCE}")
    print(f"   Destino: {BRANCH_TARGET}")
    print("-" * 50)
    
    token = get_token()
    success = create_pull_request(token)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
