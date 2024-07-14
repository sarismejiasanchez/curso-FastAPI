from fastapi import FastAPI, Body, HTTPException
# Retornar HTML
from fastapi.responses import HTMLResponse
# Creación de Esquemas
from pydantic import BaseModel
# Uso de campos Opcionales
from typing import Optional

app = FastAPI()
app.title = "Curso de FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

# Lista inicial de películas
movies = [
    {
        "id": 1,
        "title": "Dune: Parte Dos",
        "overview": "La segunda parte de la  adaptación de la novela de ciencia ficción de Frank Herbert.",
        "year": 2023,
        "rating": 8.5,
        "category": "Ciencia Ficción"
    },
    {
        "id": 2,
        "title": "Avatar: El Camino del Agua",
        "overview": "Secuela de la exitosa película de James Cameron, explorando nuevas regiones de Pandora.",
        "year": 2023,
        "rating": 8.2,
        "category": "Aventura"
    }
]


# Crear endpoint
@app.get('/', tags = ['home'])
def message():
    return HTMLResponse("<h1>Hello World!</h1>")

@app.get("/movies", tags=["movies"], response_model=list[Movie])
def get_movies():
    return movies

@app.get("/movies/{id}", tags = ["movies"])
def get_movie(id: int):
    return [movie for movie in movies if movie["id"] == id]

@app.get("/movies/", tags = ["movies"])
def get_bovies_by_category(category: str, rating: float):
    return [movie for movie in movies if movie["category"] == category and movie["rating"] >= rating]

@app.post("/movies", tags = ["movies"])
def create_movie(movie: Movie):
    new_movie = movie.model_dump()
    # Asignar un nuevo id único
    new_movie["id"] = len(movies) + 1
    # Agregar la película al final de la lista
    movies.append(new_movie)
    # Retornar la película que se acaba de crear
    return new_movie                   

@app.put("/movies/{id}", tags=["movies"], response_model=Movie)
def update_movie(id: int, movie: Movie):
    for index, item in enumerate(movies):
        if item["id"] == id:
            updated_movie = movie.model_dump()
            updated_movie["id"] = id
            movies[index] = updated_movie  # Actualizar el diccionario en la lista
            return updated_movie  # Retornar el diccionario actualizado
    
    # Si no se encuentra la película, lanzar una excepción HTTP 404
    raise HTTPException(status_code=404, detail="Movie not found")



@app.delete("/movies/{id}", tags = ["movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
        
    return movies
            