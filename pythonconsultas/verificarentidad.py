from crate import client
import sys
import numpy as np
import pandas as pd

entidad=sys.argv[1]
fichero = open('/api/config.txt')
URL = fichero.readlines(1)
connection = client.connect(
    URL[0], username="crate", timeout=5)
cursor = connection.cursor()
consulta = "SELECT entity_id FROM doc.etpersona where entity_id=? order by fecha_inicio;"
cursor.execute(consulta,(entidad,))

cabecera = [column[0] for column in cursor.description]
result = cursor.fetchall()
largo = len(result)
print(largo>0)