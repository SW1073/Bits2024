from db import DBManager
from form_model import FormModel

class Controller:
    def __init__(self):
        self.db = DBManager('prova.db', 'schema2.sql', 'Data/dades.csv')

    def get_alumnes(self, uf_id):
        return self.db._execute_query(f"SELECT COUNT(*) FROM daily_log")

    def post_daily_log(self, institut, curs, log: FormModel):
        class_id = self.db._execute_query("SELECT id FROM class c where c.centre == ? AND c.curs == ?", (institut, curs))[0][0];
        instance = self.db._execute_query("SELECT * FROM daily_log d WHERE d.fk_id_class == ? && d.date == ?", (class_id, datetime.now().date()))
        print(instance)
        # instance = self.db._execute_query("", (,))
