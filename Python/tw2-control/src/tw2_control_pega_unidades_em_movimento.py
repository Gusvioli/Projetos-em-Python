# <span class="text">G-A001 (479 | 530)</span>
import requests


def pega_unidades_em_movimento(driver, By, time):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class='icon-60x60-units']").click()
    time.sleep(2)
    ver = driver.find_element(By.TAG_NAME, "table")
    # for ler in ver:
    print(ver.text)