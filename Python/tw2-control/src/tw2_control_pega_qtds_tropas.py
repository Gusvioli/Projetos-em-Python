def pega_qtds_tropas(driver, By, time):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "icon-60x60-overview").click()
    time.sleep(2)
    for comp in driver.find_elements(By.XPATH, "//a[@href='#']"):
        if comp.text == 'Aldeias':
            comp.click()
            break
    time.sleep(2)

    vilages = []
    tropas = []
    dict = {}

    for comp in driver.find_elements(By.XPATH, "//div[@class='village']"):
        vilages.append(comp.text.replace('\n', ''))

    for comp in driver.find_elements(By.XPATH, "//td[@class='column-unit']"):
        tropas.append(comp.text)

    def divideLista(tropas):
        for y in range(0, len(tropas), 13):
           yield tropas[y:y + 13]

    tropas = list(divideLista(tropas))

    for l1, l2 in zip(vilages, tropas):
        dict[l1]= {
            'lanceiro': {'qtds': int(l2[0] if l2[0].find(
        '.') == -1 else int(l2[0].text.replace('.', '')))},
            'espada': {'qtds': int(l2[1] if l2[1].find(
        '.') == -1 else int(l2[1].text.replace('.', '')))},
            'barbaro': {'qtds': int(l2[2] if l2[2].find(
        '.') == -1 else int(l2[2].text.replace('.', '')))},
            'arqueiro': {'qtds': int(l2[3] if l2[3].find(
        '.') == -1 else int(l2[3].text.replace('.', '')))},
            'cavalaria_leve': {'qtds': int(l2[4] if l2[4].find(
        '.') == -1 else int(l2[4].text.replace('.', '')))},
            'cavalaria_arqueira': {'qtds': int(l2[5] if l2[5].find(
        '.') == -1 else int(l2[5].text.replace('.', '')))},
            'cavalaria_pesada': {'qtds': int(l2[6] if l2[6].find(
        '.') == -1 else int(l2[6].text.replace('.', '')))},
            'ariete': {'qtds': int(l2[7] if l2[7].find(
        '.') == -1 else int(l2[7].text.replace('.', '')))},
            'catapulta': {'qtds': int(l2[8] if l2[8].find(
        '.') == -1 else int(l2[8].text.replace('.', '')))},
            'berserker': {'qtds': int(l2[9] if l2[9].find(
        '.') == -1 else int(l2[9].text.replace('.', '')))},
            'trabuco': {'qtds': int(l2[10] if l2[10].find(
        '.') == -1 else int(l2[10].text.replace('.', '')))},
            'nobre': {'qtds': int(l2[11] if l2[11].find(
        '.') == -1 else int(l2[11].text.replace('.', '')))},
            'paladino': {'qtds': int(l2[12] if l2[12].find(
        '.') == -1 else int(l2[12].text.replace('.', '')))}
        }
    
    print('Dados das tropas coletados com sucesso!')

    return dict
