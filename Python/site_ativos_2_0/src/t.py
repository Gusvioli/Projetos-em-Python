import time
import pickle

# Função para salvar o estado
def salvar_estado(nome_arquivo, estado):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(estado, arquivo)

# Função para carregar o estado
def carregar_estado(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return None

# Função principal
def meu_programa():
    estado = carregar_estado('estado.pkl')

    if estado is None:
        estado = {'contador': 0}

    print(f"Início do programa. Contador atual: {estado['contador']}")

    try:
        while estado['contador'] < 10:
            estado['contador'] += 1
            print(f"Processando... Contador: {estado['contador']}")
            salvar_estado('estado.pkl', estado)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")

    print("Fim do programa.")

# Executar o programa
meu_programa()
