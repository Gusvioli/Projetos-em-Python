import shutil
import os

# Esse organizador de arquivos está funcionando porem está incompleto, estou trabalhando nele aos poucos...


def organizar_arquivos(pasta):

    add_list = []
    add_list_1 = []
    add_list2 = []
    add_list3 = []
    add_list4 = []
    add_list5 = []
    add_list_arq_cri = []
    x = 0

    # Varrer arquivos e armazenar na lista add_list
    for diretorio, subpastas, arquivos in os.walk(pasta):
        add_list4.append(subpastas)
        for arquivo in arquivos:
            # Juntar diretorio e arquivo
            caminho_arqivo = os.path.join(diretorio, arquivo)
            # Separar extenções
            cami_arqi_split = os.path.splitext(caminho_arqivo)
            # Adicionar na lista(add_list=[]) diretórios + arquivos separados
            add_list.append(cami_arqi_split)
            # Adicionar na lista(add_list_1=[]) estenções separados
            add_list_1.append(cami_arqi_split[1].replace(".", ""))
            # Adicionar na lista(add_list3=[]) diretórios + arquivos juntados
            add_list3.append(caminho_arqivo)

    # Alerar nome com caracteres da variável caracters_lista e armazenar na lista add_list2 + a extenção
    for troca in add_list:
        # Alterar caracteres ",","=","." para "_" no arquivo
        cami_arq_split_0 = troca[0].replace(",", "_")
        cami_arq_split_1 = cami_arq_split_0.replace("=", "_")
        cami_arq_split_2 = cami_arq_split_1.replace(".", "_")
        # Alterar caracteres ",","=","." para "_" na estençao
        cami_arq_split_0 = troca[1].replace(",", "_")
        cami_arq_split_0_1 = cami_arq_split_0.replace("=", "_")
        # Adicionar na lista(add_list2=[]) diretórios + arquivos ja formatados
        add_list2.append(f"{cami_arq_split_2}{cami_arq_split_0_1}")

    # Renomear arquivos antigos pelo os arquivos formatados
    while x < len(add_list):
        os.renames(f"{add_list3[x]}", f"{add_list2[x]}")
        x += 1

    """for ver_igual in add_list3:
        ver_igual_split = os.path.split(ver_igual)
        if ver_igual_split[1] == ver_igual_split[1]:
            """

    # Criar diretórios e mover os arquivos pro diretório respectivos
    for ver_dir in add_list2:
        # Separar diretórios de extenções
        ver_dir_1_ = ver_dir.split(".")
        # Verificar se existe o diretório
        if not os.path.exists(ver_dir[1]):
            try:
                # Cria arquivo
                nome_arq = f"{pasta}{ver_dir_1_[1]}"
                os.mkdir(nome_arq)
                add_list_arq_cri.append(nome_arq)
            except FileExistsError:
                pass
            # Verifica se a extenção e igual o nome do diretório
            if ver_dir_1_[1] == ver_dir_1_[1]:
                try:
                    # Move os arquivos de acordo com a extenção
                    move_dest = f"{pasta}{ver_dir_1_[1]}"
                    shutil.move(ver_dir, move_dest)
                except:
                    pass
    # Mover os arquivos repedidos e as pastas para uma o diretório "Arquivos_salvos"
    ver = os.listdir(pasta)
    vers = list(set(ver) - set(add_list_1))
    if not os.path.exists(ver_dir[1]):
        try:
            # Cria arquivo
            nome_arq_salvos = f"{pasta}Arquivos_salvos"
            os.mkdir(nome_arq_salvos)
        except FileExistsError:
            pass
    for mov in vers:
        shutil.move(f"{pasta}{mov}", f"{pasta}Arquivos_salvos")


organizar_arquivos("F:\\Dir\\")
