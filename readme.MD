# Proyecto FastAPI

## Integrantes
- Marco Tignanelli
- Juan Brusasca
- Agustin Vecchiet

## Instalación de Dependencias

1. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
2. Activa el entorno virtual:
    - En Windows (powershell):
        ```bash
        .\venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Levantar el Servidor

1. Ejecuta el servidor de FastAPI (desde el root del proyecto):
    ```bash
    uvicorn main:app --reload
    ```
2. El servidor estará corriendo en `http://127.0.0.1:8000`.

## Visualizar Swagger

1. Abre tu navegador y navega a:
    ```url
    http://127.0.0.1:8000/docs
    ```
2. Aquí podrás visualizar y probar las diferentes funciones de la API.

## Ejecutar Funciones

1. En la interfaz de Swagger, selecciona la función que deseas probar.
2. Completa los parámetros necesarios y haz clic en "Execute".
3. Revisa la respuesta de la API directamente en la interfaz.
