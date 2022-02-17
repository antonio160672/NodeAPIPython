from crate import client
import sys
import numpy as np
import pandas as pd
import json
infonode=sys.argv
#print(infonode)
indice=infonode[1]
fichero = open('/api/config.txt')
URL = fichero.readlines(1)
connection = client.connect(
    URL[0], username="crate", timeout=5)
cursor = connection.cursor()
consulta = "SELECT cintura, mano, pierna FROM doc.etpersona where entity_id=? group by cintura, mano, pierna HAVING  COUNT()>1 limit 100;"
cursor.execute(consulta,(indice,))
result = cursor.fetchall()
cabecera = [column[0] for column in cursor.description]
dispositivosPd = pd.DataFrame(result)
dispositivosPd.columns = cabecera
dispositivosPd=dispositivosPd.to_json(orient = 'columns')

consulta2="SELECT MIN(fecha_inicio) as Inicio ,MAX(fecha_fin)as Fin FROM doc.etpersona where entity_id=?;"
cursor.execute(consulta2,(indice,))
cabecera2 = [column[0] for column in cursor.description]
result2 = cursor.fetchall()
fechasPD = pd.DataFrame(result2)
fechasPD.columns = cabecera2
fechasPD=fechasPD.to_json(orient = 'columns')
dic = {
    "dispositivos": dispositivosPd,
    "fechas": fechasPD,
}
data = json.dumps(dic, sort_keys=True)
print(data)