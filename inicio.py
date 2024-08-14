import os
import subprocess
import sys

# Definir contenido para el archivo .env
env_content = """\
DB_NAME=test
DB_USER=usermain
DB_PASSWORD=12345abcd
DB_HOST=localhost
DB_PORT=5432
"""

# Nombre del archivo .env
env_file = '.env'

# Verificar si el archivo .env ya existe
if not os.path.exists(env_file):
    with open(env_file, 'w') as file:
        file.write(env_content)
    print(f'Archivo {env_file} creado exitosamente con las variables de entorno.')
else:
    print(f'El archivo {env_file} ya existe.')

# Nombre del entorno virtual
venv_dir = '.venv'

# Verificar si el entorno virtual ya existe
if not os.path.exists(venv_dir):
    # Crear el entorno virtual
    subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
    print(f'Entorno virtual {venv_dir} creado exitosamente.')
else:
    print(f'El entorno virtual {venv_dir} ya existe.')

# Activar el entorno virtual y luego instalar las librerías desde requirements.txt
def install_requirements():
    # Comando para instalar las librerías desde requirements.txt
    pip_command = [os.path.join(venv_dir, 'Scripts', 'pip.exe'), 'install', '-r', 'requirements.txt']
    
    if not os.path.exists('requirements.txt'):
        print('El archivo requirements.txt no se encuentra en el directorio.')
        return
    
    # Instalar las librerías
    subprocess.check_call(pip_command)
    print('Librerías instaladas exitosamente.')

# Ejecutar la instalación de librerías
install_requirements()