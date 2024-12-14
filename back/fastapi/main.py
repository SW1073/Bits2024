from typing import Union
from db import DBManager

from pydantic import BaseModel
from fastapi import FastAPI

class FormModel(BaseModel):
    alumne_id: int
    answers: str

app = FastAPI()
db = DBManager('prova.db')

@app.get("/")
def read_root():
    return {"hola": db.get_alumnes(3)}


@app.get("/uf/{id_uf}")
def get_uf(id_uf: int):
    return {"item_id": id_uf}

@app.get("/classe/{id_classe}")
def get_classe_alumne(classe_id: int):
    return {"item_id": item_id, "q": q}

@app.get("alumne/{id_alumne}")
def get_alumne(id_alumne: int):
    return {"result": "OK"}

@app.post("/formulari")
def get_alumne(form: FormModel):
    return {"result": "OK"}
