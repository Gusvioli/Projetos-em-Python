import socket
import os

entrada = input("1=Disparar teste de portas ou 2=Teste de porta unitária:")
ipAddress = input("Digite o IP:")

if entrada == "1":
    for ports in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if s.connect_ex((ipAddress, ports)) == 0:
            print(f"Porta {ports} Aberta!")
            arquivos = open("Portas_abertas.txt", "a")
            arquivos.write(f"\nPorta {ports} Aberta!")
            arquivos.close()
            s.close()
        else:
            print(f"Porta {ports} Fechada!")
            arquivos = open("Portas_Fechadas.txt", "a")
            arquivos.write(f"\nPorta {ports} Fechada!")
            arquivos.close()
else:
    pass
if entrada == "2":
    while True:
        entrada_ip = input("Digite a PORTA:")
        try:
            if int(entrada_ip) > 0 and int(entrada_ip) <= 65535:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ver_s = s.connect_ex((ipAddress, int(entrada_ip)))
                if ver_s == 0:
                    print(f"Porta {entrada_ip} Aberta!")
                else:
                    print(f"Porta {entrada_ip} Fechada!")
            else:
                print("PROGRAMA ENCERRADO")
                break
        except:
            pass
else:
    pass
