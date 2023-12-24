import time
from separar_dominios import executar
from contar_url_ativas import contar

tempo = 30
x = 1

while True:
    try:
        executar()
        print(f'N-{x} Executou em: {time.strftime("%d/%m/%Y %H:%M:%S")}')
        x += 1
        time.sleep(tempo) 
    except Exception as e:
        print(e)