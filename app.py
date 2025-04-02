from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

movies = [
    {"id": 1, "title": "Интерстеллар", "genre": "Фантастика", "rating": 9.0},
    {"id": 2, "title": "Начало", "genre": "Триллер", "rating": 9.8},
    {"id": 3, "title": "Матрица", "genre": "Фантастика", "rating": 8.7},
    {"id": 4, "title": "Таксист", "genre": "Криминал", "rating": 8.5},
    {"id": 5, "title": "Властелин колец1", "genre": "Фантастика", "rating": 5.8},
    {"id": 6, "title": "Властелин колец2", "genre": "Фантастика", "rating": 2.8},
    {"id": 7, "title": "Властелин колец3", "genre": "Фантастика", "rating": 8.8},
    {"id": 8, "title": "Властелин колец4", "genre": "Фантастика", "rating": 8.8},
    {"id": 9, "title": "Властелин колец5", "genre": "Фантастика", "rating": 7.8},
    {"id": 10, "title": "Властелин колец6", "genre": "Фантастика", "rating": 8.8},
    {"id": 11, "title": "Властелин колец7", "genre": "Фантастика", "rating": 3.8},
    {"id": 12, "title": "Властелин колец", "genre": "Фантастика", "rating": 8.8},
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request, "index.html", {"message": "Добро пожаловать!!", 'title': 'Главная'}
    )


@app.get("/movies/", response_class=HTMLResponse)
async def movies_list(request: Request):
    return templates.TemplateResponse(
        request, "movies.html", {"movies": movies, 'title': 'Фильмы'}
    )


@app.get("/movies/{movie_id}", response_class=HTMLResponse)
async def movie_detail(request: Request, movie_id: int):
    """
    Movie detail
    """
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if not movie:
        return templates.TemplateResponse(
            request, "404.html", {'title': 'Фильмы'}
        )

    return templates.TemplateResponse(
        request, "movie_detail.html", {"movie": movie, 'title': 'Фильмы'}
    )

if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=8000)
