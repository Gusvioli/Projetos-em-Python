import random
import string

def gerar_senha(tamanho=24):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso
senha_forte = gerar_senha()
print(senha_forte)