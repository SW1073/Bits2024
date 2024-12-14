from fastapi import FastAPI

from form_model import FormModel
from controller import Controller


app = FastAPI()
ctrl = Controller()

# Retornem l'id de l'alumne
@app.get("/alumne/{nom_alumne}")
def get_alumne(nom_alumne: str):
    return {"id": 0}

# Actualitzem la instància de daily log
@app.post("/logform/{id_alumne}")
def post_form(id_alumne: int, data):
    f = FormModel(data)
    ctrl.insert_daily_log(id_alumne, f)
