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
x = 1
n = []
while x <= 1:
    n.append(random.sample(range(1,60), 6))
    x+=1
n[0].sort()
print(n[0])

