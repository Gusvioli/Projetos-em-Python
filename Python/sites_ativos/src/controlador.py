import time
from separar_dominios import executar
from contar_url_ativas import contar

tempo = 60 * 10
x = 1
while True:
    try:
        executar()
        print(f'N-{x} Executou em: {time.strftime("%d/%m/%Y %H:%M:%S")} total de urls: {contar()} paginas ativas')
        x += 1
        time.sleep(tempo) 
    except Exception as e:
        print(e)