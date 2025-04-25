from fastapi import FastAPI
from routers import auth, places

app = FastAPI()

# Подключение роутеров
app.include_router(auth.router)
app.include_router(places.router)
