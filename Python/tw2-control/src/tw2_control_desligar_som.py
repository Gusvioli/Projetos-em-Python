from selenium.webdriver.common.keys import Keys

def desligar_som(drive, By, time,  ActionChains):
    time.sleep(5)
    drive.find_element(By.XPATH, "//a[@tooltip-content='Configurações']").click()
    time.sleep(1)
    drive.find_element(By.XPATH, "//span[@class='icon-44x44-settings-game']").click()
    time.sleep(2)
    x = 0
    while x < 25:
        time.sleep(0.2)
        ActionChains(drive).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        x += 1
    time.sleep(2)
    ActionChains(drive).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    time.sleep(2)
    ActionChains(drive).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
    time.sleep(1)
    print("Som desligado!")