# WpKiller
WpKiller es una herramienta de enumeración para WordPress que detecta la versión y múltiples endpoints expuestos de la API REST. Compatible con Linux y Windows y escrito en python

## Roadmap
- [ ] Test

## Instalación

1. Clona el repositorio
   ```sh
   git clone https://github.com/k4ixer/WpKiller
   cd WpKiller
   ```
2. Crea un entorno virtual
   ```sh
   python3 -m venv .
   ```
3. Activa el entorno virtual
     #### Linux
     ```sh
     source ./bin/activate
     ```
     #### Windows
     ```sh
     .\Scripts\activate
     ```
4. Instala las dependencias
   ```sh
   pip install -r requirements.txt
   ```
5. Ejecuta la herramienta
  ```sh
  python3 wpkiller.py
  ```
## Uso

Al ejecutar la herramienta se te pedira la URL del sitio. Aquí debes poner la dirección completa del sitio WordPress que quieres analizar:
<img width="1055" height="489" alt="image" src="https://github.com/user-attachments/assets/b74bd2f5-332d-4161-bb44-ec556acdeff8" />
## Resultado
<img width="975" height="532" alt="image" src="https://github.com/user-attachments/assets/da7fa5b9-b8b3-4d4a-b82e-c937ea8e67ee" />


