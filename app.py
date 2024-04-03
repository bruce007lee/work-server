from fastapi import FastAPI
from controller import main, api

app = FastAPI()

app.include_router(main.router)
app.include_router(api.router)
