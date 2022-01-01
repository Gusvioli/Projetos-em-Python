import random as rd


def adivinharumero():
    while True:
        x = rd.randint(0, 10)
        inx = int(input("Digite um numero:"))
        if inx == x:
            print("Seu chute acertou!!!")
            break
        else:
            print(
                "O numero é {} Não foi dessa vez tente novamente, digite outro numero:".format(x))
            continue


adivinharumero()
