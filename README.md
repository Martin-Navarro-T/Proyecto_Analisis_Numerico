# Proyecto Análisis Numérico - Autor: Martin Navarro

## Pasos a seguir en la terminal (SI USAS WINDOWS)

### Primer Paso: Descargar carpeta 

### Segundo Paso: Abrir Visual Studio Code

### Tercer Paso: Abrir una nueva terminal y poner este comando:
pip install colorama numpy sympy

### Cuarto Paso: Ejecutar el archivo main.py 

## Nota: Importante tener instalado Python para instalar las librerias con el pip install



## Pasos a seguir en la terminal (SI USAS LINUX)

### Primer paso (Clonar/Descargar carpeta)
git clone git@github.com:Martin-Navarro-T/Proyecto_Analisis_Numerico.git

## Nota: si ya tenes la carpeta descargada segui desde estos pasos

### Segundo paso (Ubicarte en la carpeta)
cd Proyecto_Analisis_Numerico

### Tercer paso (Descargar librerias y crear entorno virtual)
./install.sh

### Cuarto paso (Activar entorno virtual)
source env/bin/activate

### Quinto Paso (Para asegurar que todo se haya instalado correctamente)
./install.sh

### Sexto Paso (Para Ejecutar el Codigo)
./boot.sh

## Nota: En caso que el ./boot.sh no funcione, para ejecutar el programa podes usar:
python3 main.py

## Nota: En caso que ./install.sh no funcione y las librerias no se instalen
pip install colorama numpy sympy
