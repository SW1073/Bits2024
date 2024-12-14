import sqlite3
import os
import pandas as pd
from datetime import datetime

from form_model import FormModel


class DBManager:
    def __init__(self, path_db, path_schema, path_src):
        self.path = path_db
        self.schema = path_schema
        self.csv_src = path_src
        self._connect()
        # self._execute_query("INSERT INTO municipality(id) VALUES (?)", ('Municipi de la fib',));

    def _connect(self):
        create_tables = False
        if (not os.path.exists(self.path)):
            create_tables = True

        self.con = sqlite3.connect(self.path, check_same_thread=False)
        self.cursor = self.con.cursor()

        if create_tables:
            self._create_tables()
            self._populate_db_with_csv(self.csv_src)

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
        with open(self.schema) as file:
            query = file.read().strip()

            queries = query.split(';')
            for q in queries:
                print(q)
                self._execute_query(q)

    def _populate_db_with_csv(self, csv_path):
        try:
            df = pd.read_csv(csv_path, encoding = "utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(csv_path, encoding = 'latin1')

        for row in df.itertuples():
            n = self._execute_query("SELECT COUNT(*) FROM class c where c.centre == ? AND c.curs == ?", (row.institut, row.curs));
            if (n[0][0] == 0):
                self._execute_query("INSERT INTO class(curs, centre, municipi) VALUES(?, ?, ?)", (row.curs, row.institut, row.municipi))
            class_id = self._execute_query("SELECT c.id FROM class c where c.centre == ? AND c.curs == ?", (row.institut, row.curs))[0][0];

            print(f"KK = {class_id} {row.timestamp} {row.institut} {row.curs}")
            self._execute_query("""
INSERT INTO daily_log(event_date, fk_id_class, num_alumnes, mal_de_panxa, calfreds, mal_de_cap, mal_de_coll, mocs, nas_tapat, esternut, vomits, altres, be, regular, malament, tos) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
""", (row.timestamp, class_id, row.num_alumnes, row.mal_de_panxa, row.calfreds, row.mal_de_cap, row.mal_de_coll, row.mocs, row.nas_tapat, row.esternut, row.vomits, row.altres, row.be, row.regular, row.malament, row.tos))

