from tw2_control_pegar_relatorios import pegar_relatorios
from utils.model_jsons import pegar_armazem

from tw2_control_pega_qtds_tropas import pega_qtds_tropas

from tw2_control_pega_unidades_em_movimento import pega_unidades_em_movimento

from utils.tw2_control_criar_json import criar_json
from tw2_control_desligar_som import desligar_som
from tw2_control_pegar_valores_do_armazem import pegar_valores_do_armazem
from tw2_control_login import login
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def executar():
    driver = webdriver.Chrome()

    driver.get("https://br.tribalwars2.com/")
    try:
        login(driver, By, Keys, time, "Grallyan", "gus15935728460000gus")

        desligar_som(driver, By, time, ActionChains)

        criar_json(pegar_valores_do_armazem(
            driver, By, time, pegar_armazem, ActionChains), 'data/armazem.json')

        # criar_json(pega_qtds_tropas(driver, By, time),
        #            'data/unidades_de_tropas.json')
        
        criar_json(pegar_relatorios(driver, By, time, Keys, ActionChains), 'data/relatorios.json')

        # pega_unidades_em_movimento(driver, By, time)

        time.sleep(900)
        driver.quit()
    except Exception as e:
        print(f'Erro(s): {e}')
        time.sleep(1)
        driver.quit()
        time.sleep(10)
        return executar()


executar()
