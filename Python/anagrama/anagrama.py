from palavras_geradas_anagrama import palavras_geradas_anagrama

def calcularanagrama(nome):
    def fatorar(numero):
        z = 1
        for x in range(0, numero):
            z = z * (x + 1)
        return z

    def contar_letra_repetida(nome):
        contador = {}
        ar = []
        resultado = 0
        for letra in nome:
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1

        for x in contador:
            ar.append(contador[x])

        for n in ar:
            if n > 1:
                resultado += n

        return resultado

    def dividir_por_fator(a, b):
        return a/b

    cima = fatorar(len(nome))
    baixo = fatorar(contar_letra_repetida(nome))
    # return int(dividir_por_fator(cima, baixo))

    print(int(dividir_por_fator(cima, baixo)))

# print(f'o anagrama de \'{nome}\'é {qtds} combinações!')
# print(f'As palavras geradas foram salvas no arquivo \'palavras_anagrama.json\'')
# print('Obrigado por usar o programa!')

# from palavras_geradas_anagrama import palavras_geradas_anagrama

# import math

# def calcular_anagrama(nome):
#     def contar_letra_repetida(nome):
#         contador = {}
#         resultado = 0
#         for letra in nome:
#             if letra in contador:
#                 contador[letra] += 1
#             else:
#                 contador[letra] = 1

#         for n in contador.values():
#             if n > 1:
#                 resultado += n

#         return resultado

#     cima = math.factorial(len(nome))
#     baixo = math.factorial(contar_letra_repetida(nome))
#     return cima // baixo  # Usando // para obter uma divisão inteira

# nome = "Gerador de Anagramas"  # Substitua pelo nome desejado
# resultado = calcular_anagrama(nome)
# print(resultado)


