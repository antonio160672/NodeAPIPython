from crate import client
import sys
import numpy as np
import pandas as pd
import json
infonode=sys.argv
#print(infonode)
indice=infonode[1]
connection = client.connect(
    "http://187.188.90.137:4200/", username="crate", timeout=5)
cursor = connection.cursor()
consulta = "SELECT cintura, mano, pierna FROM doc.etpersona where entity_id=? group by cintura, mano, pierna HAVING  COUNT()>1 limit 100;"
cursor.execute(consulta,(indice,))
result = cursor.fetchall()
consulta2="SELECT MIN(fecha_inicio),MAX(fecha_fin) FROM doc.etpersona where entity_id=?;"
cursor.execute(consulta2,(indice,))
result2 = cursor.fetchall()
info=[]
for res in result:
   for data in res:
       if data:info.append(data)
       
dic = {
    "dispositivos": list(info),
    "fechas": list(result2[0]),
}
data = json.dumps(dic, sort_keys=True)
print(data)