import random as rnd

numeros_mais_sorteados = [10, 53, 5, 37, 34, 33, 23, 4, 44, 42, 30, 32, 35, 38, 41, 17]

def gerar_numeros_mega_sena(qtds_de_jogos: int = 4) -> dict:
    jogos = []
    
    for _ in range(qtds_de_jogos):
        jogos.append(rnd.sample(numeros_mais_sorteados, k=6))
    
    for _ in range(2):
        jogos.append(rnd.sample(range(1, 61), 6))
    
    return {
        'jogos 1: ': jogos[0],
        'jogos 2: ': jogos[1],
        'jogos 3: ': jogos[2],
        'jogos 4: ': jogos[3],
        'jogos 5: ': jogos[4],
        'jogos 6: ': jogos[5], 
    }

ver = gerar_numeros_mega_sena()
print(ver)