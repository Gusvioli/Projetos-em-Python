from datetime import *
import random

dia = date.today().day
mes = date.today().month
ano = date.today().year
hora = datetime.today().hour
min = datetime.today().minute
seg = datetime.today().second

lo = 1
while lo <= 10:
    dma = "Data e hora do jogo: {}/{}/{} {}:{}:{}".format(
        dia, mes, ano, hora, min, seg)
    print("\nEscolha seu jogo:\n")
    qual_Jogo = input(
        "0 = Mega sena\n1 = Quinna\n2 = Lotofácil\n3 = Lotomania\n4 = Timemania\n5 = Dupla Sena\n6 = Dia de Sorte\n7 = Super Sete\n")
    valor = input("Digite quantos jogos voce gostaria:")

    x = 1
    n = []
    n.append(dma)
    if qual_Jogo == "0":
        numero = input("Digite quantos numeros voce gostaria de jogar de 6 a 15:")
        if int(numero) >= 5 and int(numero) <= 15:
            while x <= int(valor):
                n.append(random.sample(range(1, 60), int(numero)))
                x += 1
            print("\n{}\nJogos: \n{}\n".format(n[0], n[1:]))
        else:
            print("Digite de 6 a 15 numeros, tente novamente")
    elif qual_Jogo == "1":
        numero = input("Digite quantos numeros voce gostaria de jogar de 5 a 15:")
        if int(numero) >= 5 and int(numero) <= 15:
            while x <= int(valor):
                n.append(random.sample(range(1, 60), int(numero)))
                x += 1
            print("\n{}\nJogos: \n{}\n".format(n[0], n[1:]))
        else:
            print("Digite de 5 a 15 numeros, tente novamente")

    elif qual_Jogo == "2":
        numero = input("Digite quantos numeros voce gostaria de jogar de 15 a 20:")
        if int(numero) >= 15 and int(numero) <= 20:
            while x <= int(valor):
                n.append(random.sample(range(1, 25), int(numero)))
                x += 1
            print("\n{}\nJogos: \n{}\n".format(n[0], n[1:]))
        else:
            print("Digite de 15 a 20 numeros, tente novamente")
    elif qual_Jogo == "3":
        numero = input("Digite quantos numeros voce gostaria de jogar max 50:")
        if int(numero) <= 50:
            while x <= int(valor):
                n.append(random.sample(range(1, 100), int(numero)))
                x += 1
            print("\n{}\nJogos: \n{}\n".format(n[0], n[1:]))
        else:
            print("Digite 50 numeros, tente novamente")
    elif qual_Jogo == "4":
        numero = input("Digite quantos numeros voce gostaria de jogar 10 numeros:")
        if int(numero) == 10:
            while x <= int(valor):
                n.append(random.sample(range(1, 80), int(numero)))
                x += 1
            print("\n{}\nJogos: \n{}\n".format(n[0], n[1:]))
        else:
            print("Digite 10 numeros, tente novamente")
    elif qual_Jogo == "5":
        numero = input("Digite quantos numeros voce gostaria de jogar de 6 a 15:")
        if int(numero) >= 6 and int(numero) <= 15:
            while x <= int(valor):
                n.append(random.sample(range(1, 50), int(numero)))
                x += 1
            print("\n{}\nJogos: \n{}\n".format(n[0], n[1:]))
        else:
            print("Digite de 6 a 15 numeros, tente novamente")
    elif qual_Jogo == "6":
        numero = input("Digite quantos numeros voce gostaria de jogar de 7 a 15:")
        if int(numero) >= 7 and int(numero) <= 15:
            while x <= int(valor):
                n.append(random.sample(range(1, 31), int(numero)))
                x += 1
            print("\n{}\nJogos: \n{}\n".format(n[0], n[1:]))
        else:
            print("Digite de 7 a 15 numeros, tente novamente")
    else:
        numero = input("Digite quantos numeros voce gostaria de jogar de 7 a 21:")
        if int(numero) >= 7 and int(numero) <= 21:
            while x <= int(valor):
                n.append(random.sample(range(1, 9), int(numero)))
                x += 1
            print("\n{}\nJogos: \n{}\n".format(n[0], n[1:]))
        else:
            print("Digite de 7 a 21 numeros, tente novamente")
    lo+=1