from fastapi import FastAPI

from .database import init_db
from .router import router

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(router)
