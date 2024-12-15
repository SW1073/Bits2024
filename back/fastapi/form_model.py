# from pydantic import BaseModel
import  numpy as np

class FormModel:
    num_alumnes: int
    mal_de_panxa: int
    calfreds: int
    mal_de_cap: int
    mal_de_coll: int
    mocs: int
    nas_tapat: int
    esternut: int
    vomits: int
    altres: int
    be: int
    regular: int
    malament: int
    tos: int

    def __init__(self, f):
        print(f)
        self.num_alumnes = f[0]
        self.calfreds = f[1]
        self.mal_de_panxa = f[2]
        self.mal_de_cap = f[3]
        self.mal_de_coll = f[4]
        self.mocs = f[5]
        self.nas_tapat = f[6]
        self.esternut = f[7]
        self.vomits = f[8]
        self.altres = f[9]
        self.be = f[10]
        self.regular = f[11]
        self.malament = f[12]
        self.tos = f[13]
