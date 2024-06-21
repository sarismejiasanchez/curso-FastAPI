# API REST de Películas

## Instalar y Ejecutar la Aplicación

1. **Crea el entorno virtual:**
    ```bash
    python3 -m venv venv
    ```
2. **Activa el entorno virtual:**
    ```bash
    source venv/bin/activate
    ```
3. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Ejecutar uvicorn para iniciar la aplicación:**
    ```bash
    uvicorn main:app --reload --port 5000 --host 0.0.0.0
    ```

## Métodos HTTP

El protocolo HTTP define un conjunto de métodos de petición que indican la acción que se desea realizar para un recurso determinado del servidor.

Los principales métodos soportados por HTTP y usados comúnmente en una API REST son:

- **POST**: Crea un recurso nuevo.
- **PUT**: Modifica un recurso existente.
- **GET**: Consulta información de un recurso.
- **DELETE**: Elimina un recurso.

Estos métodos nos permiten implementar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en nuestra aplicación.

## Objetivo de la API

El proyecto consistirá en la creación de una API que proporcionará información relacionada con películas. Los principales objetivos serán:

### Consulta de Todas las Películas

Utilizaremos el método `GET` para obtener todos los datos de nuestras películas.

### Filtrado de Películas

Implementaremos la capacidad de filtrar películas por su ID y por la categoría a la que pertenecen. Utilizaremos el método `GET` junto con parámetros de ruta y query para lograr esto.

### Registro de Películas

Utilizaremos el método `POST` para registrar los datos de nuevas películas. Para manejar y validar los datos, utilizaremos los esquemas de la librería `pydantic`.

### Modificación y Eliminación

Para completar el CRUD, implementaremos las operaciones de modificación (con `PUT`) y eliminación (con `DELETE`) de datos en nuestra aplicación.

Estos métodos nos permitirán construir una API robusta y completa para la gestión de información de películas.