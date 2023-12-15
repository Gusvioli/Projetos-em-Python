from selenium.webdriver.common.keys import Keys

def pegar_valor_tamanho(time, driver, By, ActionChains):
    time.sleep(2)
    ActionChains(driver).send_keys("v").perform()
    time.sleep(2)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Armazém").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@tooltip-content='Armazém']").click()
    time.sleep(1)
    pegar_tamanho = driver.find_element(
        By.XPATH, "//span[@class='float-right value']")
    return int(pegar_tamanho.text.replace('.', ''))


def pegar_valor_nivel(driver, By, time):
    time.sleep(1)
    pegar_nivel = driver.find_element(By.CSS_SELECTOR, ".small")

    return pegar_nivel.text\
        .replace('(Nível ', '')\
        .replace(')', '')\
        .replace(' + ', '/')


def pegar_valores_do_armazem(driver, By, time, pegar_armazem, ActionChains):
    time.sleep(10)
    pegar = driver.find_elements(By.CSS_SELECTOR, ".resource-text")

    pegar_armazem["armazem"]['madeira'] = int(pegar[0].text) if pegar[0].text .find(
        '.') == -1 else int(pegar[0].text.replace('.', ''))
    
    pegar_armazem["armazem"]['barro'] = int(pegar[1].text) if pegar[1].text .find(
        '.') == -1 else int(pegar[1].text.replace('.', ''))
    
    pegar_armazem["armazem"]['ferro'] = int(pegar[2].text) if pegar[2].text .find(
        '.') == -1 else int(pegar[2].text.replace('.', ''))    

    pegar_armazem["armazem"]['tamanho'] = pegar_valor_tamanho(
        time, driver, By, ActionChains)

    pegar_armazem["armazem"]['nivel/up'] = pegar_valor_nivel(driver, By, time)

    ActionChains(driver).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()

    print('Dados do armazém coletados com sucesso!')
    return pegar_armazem    

