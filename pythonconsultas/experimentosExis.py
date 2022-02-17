from crate import client
import sys
import numpy as np
import pandas as pd
import json

fichero = open('/api/config.txt')
URL = fichero.readlines(1)
connection = client.connect(
    URL[0], username="crate", timeout=5)
cursor = connection.cursor()
cadena = "SELECT DISTINCT entity_id FROM doc.etpersona;"
cursor.execute(cadena)
result = cursor.fetchall()
dic = {
    "Experimentos": list(result),
}
data = json.dumps(dic, sort_keys=True)
print(data)
