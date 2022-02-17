
import json
from gastoenergetico.filter_counts import *
from gastoenergetico.dataformat import *
from gastoenergetico.recuperacion import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from crate import client
from sensormotion.signal import *
from sensormotion.pa import *
import sys

sys.path.append("../sensormotion")
sys.path.append("../gastoenergetico")
infonode=sys.argv
print(infonode)
indice=sys.argv[1]
epoca = float(sys.argv[2])
down=float(sys.argv[3])
up=float(sys.argv[4])
fichero = open('/api/config.txt')
URL = fichero.readlines(1)
df = recuperacionData(indice,URL[0])
(
    cinturaejesx,
    cinturaejesy,
    cinturaejesz,
    manoejesx,
    manoejesy,
    manoejesz,
    piernaejesx,
    piernaejesy,
    piernaejesz,
    time,
    sampling_rate,
) = formatData(df)


# plt.scatter(time,x)
#
# print(len(time))
# print(len(cinturaejesx))
conjunto = [
    time,
    cinturaejesx,
    cinturaejesy,
    cinturaejesz,
    manoejesx,
    manoejesy,
    manoejesz,
    piernaejesx,
    piernaejesy,
    piernaejesz,
]
s = pd.DataFrame(conjunto).T
s.columns = [
    "time",
    "cinturaejesx",
    "cinturaejesy",
    "cinturaejesz",
    "piernaejesx",
    "piernaejesy",
    "piernaejesz",
    "manoejesx",
    "manoejesy",
    "manoejesz",
]
# s.to_csv('actividades.csv', header=True, index=False)

(
    cinturaejesx_counts,
    cinturaejesy_counts,
    cinturaejesz_counts,
    manoejesx_counts,
    manoejesy_counts,
    manoejesz_counts,
    piernaejesx_counts,
    piernaejesy_counts,
    piernaejesz_counts,
    cinturaejesx_f2_counts,
    cinturaejesy_f2_counts,
    cinturaejesz_f2_counts,
    manoejesx_f2_counts,
    manoejesy_f2_counts,
    manoejesz_f2_counts,
    piernaejesx_f2_counts,
    piernaejesy_f2_counts,
    piernaejesz_f2_counts,
) = filter_counts(
    down,
    up,
    epoca,
    time,
    sampling_rate,
    cinturaejesx,
    cinturaejesy,
    cinturaejesz,
    manoejesx,
    manoejesy,
    manoejesz,
    piernaejesx,
    piernaejesy,
    piernaejesz,
)
cinturavm = []
manovm = []
piernavm = []
cinturaFvm = []
manoFvm = []
piernaFvm = []

if cinturaejesx.size > 0:
    cinturavm = vector_magnitude(
        cinturaejesx_counts, cinturaejesy_counts, cinturaejesz_counts
    )
if manoejesx.size > 0:
    manovm = vector_magnitude(
        manoejesx_counts, manoejesy_counts, manoejesz_counts)
if piernaejesx.size > 0:
    piernavm = vector_magnitude(
        piernaejesx_counts, piernaejesy_counts, piernaejesz_counts
    )

if cinturaejesx.size > 0:
    cinturaFvm = vector_magnitude(
        cinturaejesx_f2_counts, cinturaejesy_f2_counts, cinturaejesz_f2_counts
    )
if manoejesx.size > 0:
    manoFvm = vector_magnitude(
        manoejesx_f2_counts, manoejesy_f2_counts, manoejesz_f2_counts
    )
if piernaejesx.size > 0:
    piernaFvm = vector_magnitude(
        piernaejesx_f2_counts, piernaejesy_f2_counts, piernaejesz_f2_counts
    )

dic = {
    "cinturaejesx_counts": list(cinturaejesx_counts),
    "cinturaejesy_counts": list(cinturaejesy_counts),
    "cinturaejesz_counts": list(cinturaejesz_counts),
    "manoejesx_counts": list(manoejesx_counts),
    "manoejesy_counts": list(manoejesy_counts),
    "manoejesz_counts": list(manoejesz_counts),
    "piernaejesx_counts": list(piernaejesx_counts),
    "piernaejesy_counts": list(piernaejesy_counts),
    "piernaejesz_counts": list(piernaejesz_counts),
    "cinturaejesx_f_counts": list(cinturaejesx_f2_counts),
    "cinturaejesy_f_counts": list(cinturaejesy_f2_counts),
    "cinturaejesz_f_counts": list(cinturaejesz_f2_counts),
    "manoejesx_f_counts": list(manoejesx_f2_counts),
    "manoejesy_f_counts": list(manoejesy_f2_counts),
    "manoejesz_f_counts": list(manoejesz_f2_counts),
    "piernaejesx_f_counts": list(piernaejesx_f2_counts),
    "piernaejesy_f_counts": list(piernaejesy_f2_counts),
    "piernaejesz_f_counts": list(piernaejesz_f2_counts),
    "cinturavm": list(cinturavm),
    "manovm": list(manovm),
    "piernavm": list(piernavm),
    "cinturaFvm": list(cinturaFvm),
    "manoFvm": list(manoFvm),
    "piernaFvm": list(piernaFvm),
}

data = json.dumps(dic, sort_keys=True)

print(data)
# print(cinturaejesx_f2_counts)
# print(cinturaejesy_f2_counts)
# print(cinturaejesz_f2_counts)
# print("\n Valores de la mano \n")
# print(manoejesx_f2_counts)
# print(manoejesy_f2_counts)
# print(manoejesz_f2_counts)
# print("\n Valores de la pierna \n")
# print(piernaejesx_f2_counts)
# print(piernaejesy_f2_counts)
# print(piernaejesz_f2_counts)


# if "cinturavm" in globals():
#     print("cintura sin filtro: \n", cinturavm)
# if "manovm" in globals():
#     print("mano sin filtro: \n", manovm)
# if "piernavm" in globals():
#     print("pierna sin filtro: \n", piernavm)


# if "cinturaFvm" in globals():
#     print("\ncintura con filtro: \n", cinturaFvm)
# if "manoFvm" in globals():
#     print("mano con filtro: \n", manoFvm)
# if "piernaFvm" in globals():
#     print("pierna con filtro: \n", piernaFvm)
