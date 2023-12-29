import json
import time
dataCriacao = time.strftime("%d/%m/%Y %H:%M:%S")

def verificar_tam_arquivos_e_separar():
    for i in range(2, 27):
        with open(f'data/dominios/dominios{i}.json', 'r') as json_file:
            data = json.load(json_file)
            if len(data['dominios']) > 500:
                new_time_data = f'{time.strftime("%d%m%Y%H%M%S")}'
                with open(f'data/dominios/dominios{i}-{new_time_data}.json', 'w') as json_file:
                    json.dump(
                        {"data_criacao": dataCriacao, "dominios": data['dominios']},
                        json_file,
                        ensure_ascii=False,
                        indent=2
                    )
                with open(f'data/dominios/dominios{i}.json', 'w') as json_file:
                    json.dump(
                        {"data_criacao": "", "dominios": []},
                        json_file,
                        ensure_ascii=False,
                        indent=2
                    )
            else:
                pass
    
    print('(OK) Realizado a verificação e separação de arquivos')