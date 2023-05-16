from fastapi import FastAPI
from uvicorn import run

from services.service2.infrastructures.http.routers.routers import router


def create_and_start_server():
    app = FastAPI()

    app.include_router(router)

    run(app, host='0.0.0.0')
