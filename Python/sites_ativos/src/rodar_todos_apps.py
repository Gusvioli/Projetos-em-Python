import subprocess


def rodar_todos_apps():    
    scripts = ['src/app_2.py', 'src/app_3.py', 'src/app_4.py', 'src/app_5', 'src/app_6.py', 'src/app_7.py', 'src/app_8.py', 'src/app_9.py', 'src/app_10.py', 'src/app_11.py', 'src/app_12.py', 'src/app_13.py', 'src/app_14.py', 'src/app_15.py', 'src/app_16.py', 'src/app_17.py', 'src/app_18.py', 'src/app_19.py', 'src/app_20.py', 'src/app_21.py', 'src/app_22.py', 'src/app_23.py', 'src/app_24.py', 'src/app_25.py', 'src/app_26.py']

    # Inicia cada script em segundo plano
    processes = [subprocess.Popen(['python', script]) for script in scripts]

    # Aguarda todos os processos terminarem
    for process in processes:
        process.wait()

rodar_todos_apps()