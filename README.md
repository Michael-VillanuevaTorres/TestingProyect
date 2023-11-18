# Proyecto_IngenieriaSoftwareII

# Proyecto de Testing (Backend)

## Como correr el proyecto en local
### Backend

El backend se encuentra en la carpeta new_api:

(Usar un Virtual Enviroment)

1. Tener pip instalado
2. Instalar flask `sudo apt install python3-flask`
3. Instalar venv  `sudo apt install python3-venv`
4. Instanciar un entorno virtual `python3 -m venv myvenv`
5. Activar el entorno `source myvenv/bin/activate`
3. Instalar los requerimientos con `pip install -r requirements.txt`
5. Correr el proyecto con `flask run`
6. Para testear el proyecto utilizar el comando `python -m pytest` adentro de la carpeta `new_api`


#####################################################

### Frontend
Tener instalado node 18.15.00

1. Hacer `npm install` para instalar las dependecias
2. Correr  el frontend con `npm dev run`

#######################################################3
### Test de aceptación
Para realizar los tests se tiene que instalar en el ambiente virtual 
`pip install robotframework`
`pip install robotframework-selenium2library`

luego en la carpeta `robot` realizar:
`robot -d results tests/test.robot`
*cambiar tests/test por directorio y nombre del test correspondiente

REQUERIMIENTOS:
Ing Soft IITema: Bug Tracker

El bugtracker seria publico (para los clientes) y seria para multiples
productos de la PYME.

