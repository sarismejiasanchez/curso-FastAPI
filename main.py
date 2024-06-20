from fastapi import FastAPI, Body
# Retornar HTML
from fastapi.responses import HTMLResponse
# Creación de Esquemas
from pydantic import BaseModel
# Uso de campos Opcionales
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

app = FastAPI()
app.title = "Curso de FastAPI"
app.version = "0.0.1"

# Lista movies
movies = [
    {
        "id": 1,
        "title": "Dune: Parte Dos",
        "overview": "La segunda parte de la adaptación de la novela de ciencia ficción de Frank Herbert.",
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
    },
    {
        "id": 3,
        "title": "Spider-Man: A través del Spider-Verso",
        "overview": "Miles Morales se embarca en una nueva aventura a través del multiverso.",
        "year": 2023,
        "rating": 8.7,
        "category": "Animación"
    },
    {
        "id": 4,
        "title": "Oppenheimer",
        "overview": "Biografía del físico teórico J. Robert Oppenheimer y su papel en el Proyecto Manhattan.",
        "year": 2023,
        "rating": 8.9,
        "category": "Drama"
    },
    {
        "id": 5,
        "title": "The Marvels",
        "overview": "Carol Danvers, Kamala Khan y Monica Rambeau unen fuerzas en esta aventura del Universo Cinematográfico de Marvel.",
        "year": 2023,
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 6,
        "title": "Wonka",
        "overview": "Una precuela que cuenta los orígenes del excéntrico chocolatero Willy Wonka.",
        "year": 2023,
        "rating": 7.5,
        "category": "Fantasía"
    },
    {
        "id": 7,
        "title": "Indiana Jones y el Dial del Destino",
        "overview": "Indiana Jones se embarca en otra emocionante aventura arqueológica.",
        "year": 2023,
        "rating": 7.4,
        "category": "Aventura"
    },
    {
        "id": 8,
        "title": "Misión Imposible: Sentencia Mortal - Parte Uno",
        "overview": "Ethan Hunt y su equipo enfrentan una nueva misión imposible en esta entrega de la serie.",
        "year": 2023,
        "rating": 8.0,
        "category": "Acción"
    },
    {
        "id": 9,
        "title": "The Flash",
        "overview": "Barry Allen utiliza sus poderes para viajar en el tiempo y salvar a su familia, pero crea una realidad alternativa con consecuencias inesperadas.",
        "year": 2023,
        "rating": 7.3,
        "category": "Ciencia Ficción"
    },
    {
        "id": 10,
        "title": "La Sirenita",
        "overview": "Una versión en acción real del clásico animado de Disney, que cuenta la historia de Ariel, una joven sirena que sueña con vivir en la superficie.",
        "year": 2023,
        "rating": 7.1,
        "category": "Musical"
    }
]

# Crear endpoint
@app.get('/', tags = ['home'])
def message():
    return HTMLResponse("<h1>Hello World!</h1>")

@app.get('/movies', tags = ['movies'])
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
    movies.append(movie)
    
    #return [item for item in movies if item["id"] == movie.id]
    return movies                   

@app.put("/movies/{id}", tags = ["movies"])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
    
    return movies

@app.delete("/movies/{id}", tags = ["movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
        
    return movies
            