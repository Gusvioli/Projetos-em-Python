def pegar_relatorios(driver, By, time, Keys, ActionChains):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id='report-button']").click()
    time.sleep(2)
    
    for x in driver.find_elements(By.TAG_NAME, 'div'):
        if x.text == '100':
            x.click()
            break

    relatorios = []
    for relatorio in driver.find_elements(By.TAG_NAME, 'h5'):
        relatorios.append(relatorio.text)
        # relatorio.click()
        # time.sleep(2)
        # ActionChains(driver).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
        # time.sleep(2)
    print('Relatorios coletados com sucesso!')
    print(relatorios)
    return relatorios

# class="size-34x34 btn-red icon-26x26-close"