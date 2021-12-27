import time

ent_nP = input("""
1 para rodar uma sequencia Ex:. 2 100 (min e maximo)
2 pra escolher um numero e verificar se é primo
""")


if ent_nP == '1':
    ent_nP_1 = input("Escolha uma sequencia ex:. 0 100(min e maximo): ")
    ent_nP_1 = ent_nP_1.split()

    print("Uma lista de numeros primos de {} até {} será exibida".format(ent_nP_1[0], ent_nP_1[1]))
    time.sleep(4)

    x = int(ent_nP_1[0])
    x2 = int(ent_nP_1[1])
    while x <= x2:
        for n in range(2, x):
            if x % n == 0:
                break
        else:
            print(x)
        x += 1
else:
    ent_nP_2 =  int(input("Escolha um numero: "))
    time.sleep(1)
    for n in range(2, ent_nP_2):
        if ent_nP_2 % n == 0:
            print("Esse numero não é primo")
            break
    else:
        print("Esse numero é primo")