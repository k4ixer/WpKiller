"""
Nombre: WpKiller
Autor: Alejandro Herrero (aka. k4ixer)
Versión: v0.1 (Linux y Windows)
"""

import os
import requests
import time
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#FUNCIONES -> UTILIDAD
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def end():
    sys.exit()

def validate_url(target):
    try:
        r = requests.get(f"{target}", verify=False)
        if r.status_code == 404 or r.status_code == 401:
            banner()
            print("\033[91m   [+] ERROR: La URL no se encuentra disponible\033[0m")
            end()
    except requests.ConnectionError:
        banner()
        print("\033[91m   [+] ERROR: La URL no existe\033[0m")
        end()

def validate_wordpress(target):
    validate = requests.get(f"{target}/wp-includes/", verify=False)
    if validate.status_code == 404:
        banner()
        print("\033[91m   [+] ERROR: La URL no es un WordPress\033[0m")
        end()

#FUNCIONES -> PERSONALIZACIÓN
def banner():
    cls()
    print()
    print("\033[94m  ██╗    ██╗██████╗     ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗\033[0m")
    print("\033[94m  ██║    ██║██╔══██╗    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗\033[0m")
    print("\033[94m  ██║ █╗ ██║██████╔╝    █████╔╝ ██║██║     ██║     █████╗  ██████╔╝\033[0m")
    print("\033[94m  ██║███╗██║██╔═══╝     ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗\033[0m")
    print("\033[94m  ╚███╔███╔╝██║         ██║  ██╗██║███████╗███████╗███████╗██║  ██║\033[0m")
    print("\033[94m   ╚══╝╚══╝ ╚═╝         ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═╝\033[0m")
    print()

#FUNCIONES -> PROGRAMA
def enumerar(target):
    banner()

    #Versión de WordPress
    print("\033[93m   Enumerando versión de WordPress...\033[0m")
    r = requests.get(f"{target}", verify=False)
    start = r.text.find('<meta name="generator" content="WordPress')
    if start != -1:
        start_quote = r.text.find('"', start + 30) + 1
        end_quote = r.text.find('"', start_quote)
        version = r.text[start_quote:end_quote].replace('WordPress ', '')
        print()
        print(f"\033[96m   [+] Versión -> {version}\033[0m")
        print()
    else:
        print("\033[91m   [+] No se encontró versión de WordPress\033[0m")
        print()

    #Enumeración de usuarios mediante API REST
    print("\033[93m   Enumerando usuarios...\033[0m")
    found_username = 0
    api = requests.get(f"{target}/wp-json/wp/v2/users", verify=False)
    if api.status_code == 200:
        print()
        print(f"\033[96m   [+] JSON con usuarios -> {target}/wp-json/wp/v2/users\033[0m")
    else:
        found_username + 1
    
    #Enumeración de usuarios mediante author-sitemap.xml
    authorsitemap = requests.get(f"{target}/author-sitemap.xml", verify=False)
    if authorsitemap.status_code == 200:
        print()
        print(f"\033[96m   [+] XML con usuarios -> {target}/author-sitemap.xml\033[0m")
    else:
        found_username + 1

    if found_username == 2:
        print("\033[91m   [+] No se han encontrado usuarios\033[0m")
        print()

    #Comprobar si está activo xmlrpc.php
    xmlrpc = requests.get(f"{target}/xmlrpc.php", verify=False)
    if xmlrpc.status_code == 200:
        print(f"\033[96m   [+] xmlrpc.php -> {target}/xmlrpc.php\033[0m")
        print()

def enumerar_api(target):
    def enum_rest(target, ruta, nombre):
        r = requests.get(f"{target}/wp-json{ruta}", verify=False)
        if r.status_code == 200:
            print(f"\033[96m   [+] {nombre} -> {target}/wp-json{ruta}\033[0m")

    validate_api = requests.get(f"{target}/wp-json", verify=False)
    if validate_api.status_code != 200:
        print("\033[91m   [+] Sin acceso a la API REST\033[0m")
        print()
    else:
        print()
        print("\033[93m   Enumerando API REST...\033[0m")
        print()
        enum_rest(target, '/wp/v2/users', 'USUARIOS');
        enum_rest(target, '/wp/v2/posts', 'ENTRADAS');
        enum_rest(target, '/wp/v2/media', 'MEDIA');
        enum_rest(target, '/wp/v2/pages', 'PÁGINAS');
        enum_rest(target, '/wp/v2/settings', 'CONFIGURACIONES');
        enum_rest(target, '/wp/v2/comments', 'COMENTARIOS');
        enum_rest(target, '/wp/v2/categories', 'CATEGORÍAS');
        enum_rest(target, '/wp/v2/tags', 'ETIQUETAS');
        enum_rest(target, '/wp/v2/types', 'TIPOS DE CONTENIDO');
        enum_rest(target, '/wp/v2/statuses', 'ESTADOS');
        enum_rest(target, '/wp/v2/themes', 'TEMAS');
        enum_rest(target, '/wp/v2/search', 'BÚSQUEDA');
        enum_rest(target, '/wp/v2/block-types', 'TIPOS DE BLOQUES');
        enum_rest(target, '/wp/v2/blocks', 'BLOQUES');
        enum_rest(target, '/wp/v2/blocks/<id>/autosaves/', 'AUTOSAVES BLOQUES');
        enum_rest(target, '/wp/v2/block-renderer', 'RENDERIZADOR BLOQUES');
        enum_rest(target, '/wp/v2/block-directory/search', 'BÚSQUEDA DIRECTORIO BLOQUES');
        enum_rest(target, '/wp/v2/plugins', 'PLUGINS');
        print()

# FUNCIÓN -> MAIN
def main():
    global target
    banner()
    target = input("   [+] Introduce la URL del target (ej: http://example.com): ").strip()
    validate_url(target)
    validate_wordpress(target)
    enumerar(target)
    enumerar_api(target)
    print("\033[92m   [✓] Análisis completo.\033[0m")
    print("")

#EJECUCIÓN
if __name__ == "__main__":
    main()

