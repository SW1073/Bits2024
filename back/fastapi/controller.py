from db import DBManager
from form_model import FormModel
import sys
import os
sys.path.append(os.path.abspath('../../model/'))
from analyze_results import main
import subprocess
import re
import numpy as np

class Controller:
    def __init__(self):
        self.db = DBManager('prova.db', 'schema2.sql', 'Data/dades.csv')

    def extract_tensors(self, text):
        # Regular expression to match the Generated Sequence tensor
        generated_pattern = r"Generated Sequence for .*?:\s+tensor\((.*?)\)"

        # Search for the tensor in the Generated Sequence section
        match = re.search(generated_pattern, text, re.DOTALL)
        if not match:
            raise ValueError("Generated Sequence tensor not found in the text.")

        # Extract the tensor content and clean it up
        tensor_content = match.group(1).strip()

        # Convert the tensor content into a 2D list of floats
        rows = tensor_content.split("],")
        array = []
        for row in rows:
            # Remove brackets and split by commas
            clean_row = row.replace("[", "").replace("]", "").strip()
            array.append([float(x) for x in clean_row.split(",")])
        # Convert the list into a NumPy array
        return np.array(array)

    # Convert the list into a N
    def get_alumnes(self, uf_id):
        return self.db._execute_query(f"SELECT COUNT(*) FROM daily_log")

    def post_daily_log(self, institut, curs, log: FormModel):
        class_id = self.db._execute_query("SELECT id FROM class c where c.centre == ? AND c.curs == ?", (institut, curs))[0][0];
        instance = self.db._execute_query("SELECT * FROM daily_log d WHERE d.fk_id_class == ? && d.date == ?", (class_id, datetime.now().date()))
        print(instance)
        # instance = self.db._execute_query("", (,))

    def model_predict(self, class_id):
        # append csv
        # execute model
        p = subprocess.Popen( ['python3', 'analyze_results.py', '--data_path', 'result.csv', '--use_last_14_columns'], cwd="../../model/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        p.wait()
        stdout, stderr = p.communicate()
        result = self.extract_tensors(stdout)
        print(result)

        return result


    def get_prediction(self, class_id):
        return FormModel(self.model_predict(class_id)[0])
