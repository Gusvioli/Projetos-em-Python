import itertools
import requests
import time

def gerar_combinacoes(characters, dominios, tamanho):
    for combination in itertools.product(characters, repeat=tamanho):
        yield ''.join(combination)

def realizar_requisicao(nome_url_http, dominio):
    try:
        url = f'http://{nome_url_http}{dominio}'
        r_http = requests.get(url, timeout=3)
        dominio(nome_url_http, r_http.status_code, r_http.headers, r_http.url, 10)
    except Exception as e:
        print(e)

def main():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    dominios = [".com", ".net", ".org"]  # Adicione mais domínios conforme necessário

    for nome_url_http in gerar_combinacoes(characters, dominios, 26):
        realizar_requisicao(nome_url_http, dominios[0])  # Use o primeiro domínio como exemplo
        time.sleep(0.5)

if __name__ == "__main__":
    main()
