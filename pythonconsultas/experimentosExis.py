from crate import client
import sys
import numpy as np
import pandas as pd
import json

connection = client.connect(
    "http://187.188.90.137:4200/", username="crate", timeout=5)
cursor = connection.cursor()
cadena = "SELECT DISTINCT entity_id FROM doc.etpersona;"
cursor.execute(cadena)
result = cursor.fetchall()
dic = {
    "Experimentos": list(result),
}
data = json.dumps(dic, sort_keys=True)
print(data)
