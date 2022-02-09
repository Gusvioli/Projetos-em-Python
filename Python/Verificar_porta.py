import socket
import os

ipAddress = '187.67.172.51'

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
