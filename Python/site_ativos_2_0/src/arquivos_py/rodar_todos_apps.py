import sys
sys.path.append('/home/gusvioli/Documentos/projetos/Projetos-em-Python/Python/site_ativos_2_0/src/arquivos_py')

import subprocess
import time


def rodar():    
    scripts = ['src/arquivos_py/apps/app_2.py', 'src/arquivos_py/apps/app_3.py', 'src/arquivos_py/apps/app_4.py', 'src/arquivos_py/apps/app_5.py', 'src/arquivos_py/apps/app_6.py', 'src/arquivos_py/apps/app_7.py', 'src/arquivos_py/apps/app_8.py', 'src/arquivos_py/apps/app_9.py', 'src/arquivos_py/apps/app_10.py', 'src/arquivos_py/apps/app_11.py', 'src/arquivos_py/apps/app_12.py', 'src/arquivos_py/apps/app_13.py', 'src/arquivos_py/apps/app_14.py', 'src/arquivos_py/apps/app_15.py', 'src/arquivos_py/apps/app_16.py', 'src/arquivos_py/apps/app_17.py', 'src/arquivos_py/apps/app_18.py', 'src/arquivos_py/apps/app_19.py', 'src/arquivos_py/apps/app_20.py', 'src/arquivos_py/apps/app_21.py', 'src/arquivos_py/apps/app_22.py', 'src/arquivos_py/apps/app_23.py', 'src/arquivos_py/apps/app_24.py', 'src/arquivos_py/apps/app_25.py', 'src/arquivos_py/apps/app_26.py', 'src/migrations/limpar_diplicatas_no_db.py']

    # Inicia cada script em segundo plano
    processes = [subprocess.Popen(['python', script]) for script in scripts]

    # Aguarda todos os processos terminarem
    for process in processes:
        process.wait()