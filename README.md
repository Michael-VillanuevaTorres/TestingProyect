# Proyecto_IngenieriaSoftwareII

## Como correr el proyecto en local

### Backend

El backend se encuentra en la carpeta api:

(Usar un Virtual Enviroment)

1. Tener pip instalado
2. Instalar flask `sudo apt install python3-flask`
3. Instalar venv  `sudo apt install python3-venv`
4. Instanciar un entorno virtual `python3 -m venv myvenv`
5. Activar el entorno `source myvenv/bin/activate`
3. Instalar los requerimientos con `pip install -r requirements.txt`
5. Correr el proyecto con `flask run`

Para correr los test, estar dentro del entorno virtual:

1. Instalar pytest `pip install pytest`
2. Ir a la carpeta tests y con `pytest test_encargado.py`// Tambien se puede escribir pytest y se iniciaran todos los test

### Recalcar que los test no pasan las pruebas 

### Frontend
Tener instalado node 18.15.00

1. Hacer `npm install` para instalar las dependecias
2. Correr  el frontend con `npm dev run`

REQUERIMIENTOS:
Ing Soft IITema: Bug Tracker

El bugtracker seria publico (para los clientes) y seria para multiples
productos de la PYME.

