#!/bin/bash

# Crear el entorno virtual si no existe
python3 -m venv env

# Mostrar mensaje para activar el entorno virtual
echo "-> Entorno virtual creado."

# Instalar las dependencias dentro del entorno virtual
source env/bin/activate
pip install -r requirements.txt

# Mostrar mensaje final
echo "-> Instalación completa."
echo "--> Antes de ejecutar 'boot.sh', asegúrate de activar el entorno virtual, con el siguiente comando:"
echo "---> 'source env/bin/activate'"
echo "-> Nota: Después de activar el entorno virtual, ejecuta nuevamente 'install.sh'"
echo "--> Ahora para ejecutar la aplicación, ponga el siguiente comando:"
echo "---> './boot.sh'"
echo "-> Nota: Si luego deseas desactivar el entorno virtual (env) escriba ´deactivate´"

