import shutil
import os
import time


def organizar_arquivos(pasta):

    if os.path.exists(f"{pasta}CAMINHO_ORIGINAL.txt") == False:
        # Orgnizador de aarquivos por extenção
        bkpi_dir_cam_ori = []
        for diretorio, subpastas, arquivos in os.walk(pasta):

            for arquivo in arquivos:
                caminho_arqivo = os.path.join(diretorio, arquivo)
                bkpi_dir_cam_ori.append(caminho_arqivo)
                caminho_arqivo2 = os.path.splitext(caminho_arqivo)
                caminho_arqivo3 = caminho_arqivo2[0].replace(".", "_")
                caminho_arqivo4 = os.path.join(
                    caminho_arqivo3, caminho_arqivo2[1])
                caminho_arqivo5 = os.path.split(caminho_arqivo4)
                caminho_arqivo6 = f"{caminho_arqivo5[0]}{caminho_arqivo5[1]}"
                os.renames(caminho_arqivo, caminho_arqivo6)

                if os.path.exists(f"{pasta}{caminho_arqivo2[1]}".replace(".", "")) == False:
                    os.mkdir(f"{pasta}{caminho_arqivo2[1]}".replace(".", ""))
                    print(
                        f"\033[1;36mCRIANDO DIRETÓRIO:\033[0m {pasta}{caminho_arqivo2[1]} \033[;32m OK \033[m")
                    time.sleep(0.02)

                print(
                    f"\033[1;36mTRANSFERINDO ARQUIVO:\033[0m {caminho_arqivo} \033[;32m OK \033[m")
                time.sleep(0.02)
                retirar_Ponto = caminho_arqivo5[1].replace(".", "")

                if retirar_Ponto == retirar_Ponto:
                    shutil.move(caminho_arqivo6,
                                f"{pasta}{retirar_Ponto}\\{arquivo}")

        with open(f"{pasta}CAMINHO_ORIGINAL.txt", "w+") as file:
            file.write("--------------------------------\n")
            file.write("Caminho original dos arquivo\n")
            file.write("--------------------------------\n")
            for gravar in bkpi_dir_cam_ori:
                file.write(f"{gravar}\n")
        file.close()

        time.sleep(0.5)
        print(f"\033[;32mTODOS OS ARQUIVOS FORAM TRANSFERIDOS COM SUCESSO!\033[m")
        time.sleep(0.5)
    else:
        print(
            f"\033[;31mTODOS OS ARQUIVOS JÁ FORAM TRANSFERIDOS E ORGANIZADOS NO DIRETÉRIO INFORMADO!\033[m")


pasta_info = input("Digite o diretório a ser organizado(Ex:. C:\dir\ ):")
organizar_arquivos(pasta_info)
