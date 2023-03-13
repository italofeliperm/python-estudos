import chromedriver_autoinstaller
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pesquisar(texto):
    chromedriver_autoinstaller.install()
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("http://google.com")
    sleep(1)
    aceitar = driver.find_element(by=By.ID, value="L2AGLb")
    aceitar.click()
    pesquisa = driver.find_element(by=By.NAME, value="q")
    pesquisa.send_keys(texto)
    sleep(3)
    botao = driver.find_element(by=By.NAME, value="btnK")
    botao.click()
    sleep(3)
    resultados = driver.find_element(by=By.ID, value="rso")
    with open("resultados.html", "w") as f:
        dados = resultados.get_attribute("innerHTML")
        f.write(dados)
    page = driver.find_element(by=By.TAG_NAME, value="body")
    total_height = page.size["height"]
    driver.set_window_size(1920, total_height)
    page.screenshot("resultados.png")
    driver.close()


pesquisa = input("digite um termo para pesquisar: ")
pesquisar(pesquisa)
