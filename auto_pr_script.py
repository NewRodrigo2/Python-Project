#!/usr/bin/env python3
"""
Script para automatizar Pull Request de class_python a master
Crea PR, verifica conflictos y mergea automáticamente si no hay conflictos
"""

import requests
import json
import sys
from datetime import datetime

# Configuración
GITHUB_TOKEN = input("Ingresa tu Personal Access Token de GitHub: ")
REPO_OWNER = "NewRodrigo2"
REPO_NAME = "Python-Project"
SOURCE_BRANCH = "class_python"
TARGET_BRANCH = "master"

# Base URL para API de GitHub
BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

# Headers con autenticación
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json"
}


def log_message(message, level="INFO"):
    """Imprime mensajes con timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")


def create_pull_request():
    """Crea un Pull Request"""
    log_message("Creando Pull Request...")
    
    url = f"{BASE_URL}/pulls"
    payload = {
        "title": f"Merge {SOURCE_BRANCH} to {TARGET_BRANCH}",
        "body": f"Pull Request automático de `{SOURCE_BRANCH}` a `{TARGET_BRANCH}`\n\nCreado por: auto_pr_script.py",
        "head": SOURCE_BRANCH,
        "base": TARGET_BRANCH
    }
    
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        
        if response.status_code == 201:
            pr_data = response.json()
            pr_number = pr_data["number"]
            log_message(f"✅ Pull Request creado exitosamente: #{pr_number}")
            return pr_number
        elif response.status_code == 422:
            log_message("⚠️  No hay cambios para crear un PR o ya existe uno", "WARNING")
            # Intenta obtener el PR existente
            existing_pr = get_existing_pr()
            if existing_pr:
                return existing_pr
            return None
        else:
            log_message(f"❌ Error al crear PR: {response.status_code} - {response.text}", "ERROR")
            return None
    except Exception as e:
        log_message(f"❌ Excepción al crear PR: {str(e)}", "ERROR")
        return None


def get_existing_pr():
    """Obtiene un PR existente entre las dos ramas"""
    log_message("Buscando PR existente...")
    
    url = f"{BASE_URL}/pulls"
    params = {"state": "open", "head": f"{REPO_OWNER}:{SOURCE_BRANCH}", "base": TARGET_BRANCH}
    
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        
        if response.status_code == 200:
            prs = response.json()
            if prs:
                return prs[0]["number"]
        return None
    except Exception as e:
        log_message(f"Error buscando PR existente: {str(e)}", "ERROR")
        return None


def check_mergeable(pr_number):
    """Verifica si el PR puede ser mergeado (sin conflictos)"""
    log_message(f"Verificando si PR #{pr_number} puede ser mergeado...")
    
    url = f"{BASE_URL}/pulls/{pr_number}"
    
    try:
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            pr_data = response.json()
            
            if pr_data["mergeable"] is None:
                log_message("⏳ GitHub aún está analizando conflictos, esperando...", "INFO")
                import time
                time.sleep(3)
                return check_mergeable(pr_number)
            
            if pr_data["mergeable"]:
                log_message("✅ El PR puede ser mergeado (sin conflictos)")
                return True
            else:
                log_message("❌ Hay conflictos en el PR. No se puede mergear automáticamente", "ERROR")
                log_message(f"Revisa: https://github.com/{REPO_OWNER}/{REPO_NAME}/pull/{pr_number}", "INFO")
                return False
        else:
            log_message(f"Error al verificar mergeable: {response.status_code}", "ERROR")
            return False
    except Exception as e:
        log_message(f"Excepción verificando mergeable: {str(e)}", "ERROR")
        return False


def merge_pull_request(pr_number):
    """Mergea automáticamente el PR"""
    log_message(f"Mergeando PR #{pr_number}...")
    
    url = f"{BASE_URL}/pulls/{pr_number}/merge"
    payload = {
        "commit_title": f"Merge {SOURCE_BRANCH} into {TARGET_BRANCH}",
        "commit_message": f"Merge automático de {SOURCE_BRANCH} a {TARGET_BRANCH}",
        "merge_method": "merge"  # Puede ser: merge, squash, rebase
    }
    
    try:
        response = requests.put(url, headers=HEADERS, json=payload)
        
        if response.status_code == 200:
            log_message(f"✅ PR #{pr_number} mergeado exitosamente")
            return True
        else:
            log_message(f"❌ Error al mergear: {response.status_code} - {response.text}", "ERROR")
            return False
    except Exception as e:
        log_message(f"Excepción al mergear: {str(e)}", "ERROR")
        return False


def main():
    """Función principal"""
    log_message("=" * 60)
    log_message("AUTOMATIZADOR DE PULL REQUEST")
    log_message(f"Origen: {SOURCE_BRANCH} → Destino: {TARGET_BRANCH}")
    log_message("=" * 60)
    
    # Paso 1: Crear PR
    pr_number = create_pull_request()
    if not pr_number:
        log_message("No se pudo crear el PR. Abortando.", "ERROR")
        sys.exit(1)
    
    # Paso 2: Verificar si puede mergearse
    if check_mergeable(pr_number):
        # Paso 3: Mergear
        if merge_pull_request(pr_number):
            log_message("=" * 60)
            log_message("🎉 ¡Proceso completado exitosamente!")
            log_message("=" * 60)
        else:
            log_message("No se pudo mergear el PR.", "ERROR")
            sys.exit(1)
    else:
        log_message("PR no puede ser mergeado por conflictos.", "ERROR")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log_message("\n⚠️  Operación cancelada por el usuario", "WARNING")
        sys.exit(0)
    except Exception as e:
        log_message(f"❌ Error inesperado: {str(e)}", "ERROR")
        sys.exit(1)
