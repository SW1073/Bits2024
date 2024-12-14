from typing import Union
from db import DBManager
from form_model import FormModel

from fastapi import FastAPI


app = FastAPI()
db = DBManager('prova.db', 'schema2.sql')
db.populate_db_with_csv('Data/dades.csv')

@app.get("/uf/{id_uf}")
def get_uf(id_uf: int):
    return {"item_id": id_uf}

@app.get("/alumne/{id_alumne}")
def get_alumne(id_alumne: int):
    return {"result": "OK"}

@app.get("/logform")
def post_form():

    # f = FormModel()
    # db.insert_daily_log(alumni_id, f)
    return {"hola": db.get_alumnes(0)}
