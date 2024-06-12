# Desarrollo de un servidor de API con FastAPI

## Descripción

FastAPI es un marco web ampliamente adoptado para crear aplicaciones web sólidas con Python. Destaca por su notable velocidad, como su nombre indica, y está categorizado como un framework web asíncrono, lo que permite a los desarrolladores crear APIs de alto rendimiento sin esfuerzo.

A diferencia de muchos otros marcos, FastAPI viene equipado con validación automática de datos, serialización y generación de documentación interactiva, lo que reduce la necesidad de herramientas o bibliotecas de terceros.

Algunas de las plataformas y servicios más conocidos, como Uber, Netflix y Starlink, han aprovechado el poder de FastAPI para crear aplicaciones de vanguardia. Profundizaremos en los aspectos centrales de FastAPI, mejorando tu repertorio de desarrollo web.

## Creación de un servidor de API básico con FastAPI

> Comprender cómo funciona FastAPI

> Creación de un modelo Pydantic

> Creación de rutas de API CRUD sencillas

> Usar Postman para probar la API

    *HTTP básico con FastAPI*
    Anteriormente, creaba una sola ruta en "/" para una página que simplemente devuelve algo de texto al recibir una solicitud GET. Sin embargo, se espera que los servidores de API tengan muchos más puntos de conexión que admitan varios métodos de solicitud para diferentes propósitos.

    Normalmente, así es como funcionan los servidores de API en el contexto de la gestión de usuarios, con referencia al marco CRUD.

    OBTENER - Leer

    POST - Crear

    PUT - Actualización

    DELETE - Eliminar

    Por ejemplo, el punto de conexión de la API para recuperar una lista de usuarios tendría el siguiente aspecto
                    GET /users
    
    Para agregar un nuevo usuario a la base de datos, podría tener el siguiente aspecto, con un cuerpo JSON.
                    POST /users

                    {
                        “username”: “antony”,
                        “email”: “antony@stackup.com”
                    }

## Enrutamiento con FastAPI
Anteriormente, usamos el siguiente código para crear el punto de conexión para devolver texto cuando se realiza una solicitud GET a "/".
@app.get("/")
def index():
    return "Hello Antony :D"

Para crear controladores para otros métodos de solicitud, todo lo que tiene que hacer es editar la parte "get" del decorador. En el caso de un punto de conexión de API para usuarios, sería:

@app.get("/users")
@app.post("/users")
@app.put("/users")
@app.delete("/users/<int:id>")

## Configuración de nuestro entorno
crear una nueva carpeta xxx y agregar :
> main.py

> models.py 

> requirements.txt  

crear entorno virtual

        python3 -m venv ./venv/
agregar a requirements
        fastapi
        uvicorn
        pydantic

despues ejecutar en terminal :      pip3 install -r requirements.txt

## Creando nuestro modelo de usuario

from pydantic import BaseModel

        class User(BaseModel):

            name: str
            
            age: int

## Desarrollo de la API

abra main.py

            from fastapi import FastAPI, status

            import uuid

            from models import User

            app = FastAPI()

            users = {

                "1": {

                    "name": "John",

                    "age": 20
                },

                "2": {

                    "name": "Jane",

                    "age": 21
                }

            }

            @app.get("/users")

            def users_list():

            return users

            @app.get("/users/{user_id}")

            def user_details(user_id: str):

            return users[user_id]

            @app.post("/users", status_code=status.HTTP_201_CREATED)

            def user_add(user: User):

             users[str(uuid.uuid4())] = user

            return "User added"

            @app.put("/users/{user_id}", status_code=status.HTTP_200_OK)

            def user_update(user_id: str, user: User):

            users[user_id] = user

            return "User updated"

            @app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)

            def user_delete(user_id: str):

            del users[user_id]

            return "User deleted"


## Ejecución de la aplicación

uvicorn main:app --reload
