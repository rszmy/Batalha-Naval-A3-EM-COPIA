from typing import Union
from fastapi import FastAPI
from controladores.main_controlador import MainControlador

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}