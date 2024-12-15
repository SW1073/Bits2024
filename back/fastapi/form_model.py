from pydantic import BaseModel

class FormModel(BaseModel):
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
        self.calfreds = f["calfreds"]
        self.mal_de_cap
        self.mal_de_coll
        self.mocs
        self.nas_tapat
        self.esternut
        self.vomits
        self.altres
        self.be
        self.regular
        self.malament
        self.tos
