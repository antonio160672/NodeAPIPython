from crate import client
import sys
import numpy as np
import pandas as pd

entidad=sys.argv[1]
connection = client.connect(
    "http://187.188.90.137:4200/", username="crate", timeout=5)
cursor = connection.cursor()
consulta = "SELECT entity_id FROM doc.etpersona where entity_id=? order by fecha_inicio limit 100;"
cursor.execute(consulta,(entidad,))

cabecera = [column[0] for column in cursor.description]
result = cursor.fetchall()
largo = len(result)
print(largo>0)