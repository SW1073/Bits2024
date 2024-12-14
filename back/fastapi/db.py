import sqlite3
import os

class DBManager:
    def __init__(self, path):
        self.path = path
        self._connect()
        self._execute_query("INSERT INTO aula(nom) VALUES (?)", ('aula de prova',));

    def _connect(self):
        create_tables = False
        if (not os.path.exists(self.path)):
            create_tables = True

        self.con = sqlite3.connect(self.path, check_same_thread=False)
        self.cursor = self.con.cursor()

        if create_tables:
            self._create_tables()

    def _execute(self, query):
        self.con = sqlite3.connect(self.path)
        self.cursor = self.con.cursor()

        if 'SELECT' in query:
            return self.cursor.execute(query).fetchall()
        else:
            self.cursor.execute(query)
            self.cursor.commit()

    def _execute_query(self, query, params=None):
        cur = self.con.cursor()
        # If there are parameters, execute with them
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)

        # For SELECT queries, fetch the results
        if query.strip().lower().startswith("select"):
            return cur.fetchall()
        else:
            # For other queries, commit the changes and return last row ID
            self.con.commit()

    def _create_tables(self):
        with open("../flaskr/schema.sql") as file:
            query = file.read().strip()

            queries = query.split(';')
            for q in queries:
                print(q)
                self._execute_query(q)


    def get_alumnes(self, uf_id):
        # return self._execute(f"SELECT * FROM alumne a WHERE a.uf_id == {uf_id}")
        return self._execute_query(f"SELECT * FROM aula")

