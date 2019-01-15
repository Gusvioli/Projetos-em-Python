import numpy as np
import pandas as pd
from datetime import *
import random

dia = date.today().day
mes = date.today().month
ano = date.today().year
hora = datetime.today().hour
min = datetime.today().minute
seg = datetime.today().second

dma = "Hora atual\n{}/{}/{} {}:{}:{}\n".format(dia,mes,ano,hora,min,seg)
print(dma)

n = []

for x in range(0,10):
    n.append(random.sample(range(1,60), 6))

nn = np.array(n)

nn2 = pd.Series(data=list(nn),index='1 2 3 4 5 6 7 8 9 10'.split())

print(nn2)


