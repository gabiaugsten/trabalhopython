from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Se estiver usando o Pycharm para desenvolvedor,
# Adicione estas linhas
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
# Passe a variavel opts para o webdriver
navegador = webdriver.Chrome(options=opts)
url = r'https://www.kabum.com.br/'
navegador.get(url)

botao = navegador.find_element(By.ID, "onetrust-accept-btn-handler")
botao.click()

search_box = navegador.find_element(By.TAG_NAME, "input")
search_box.clear()
search_box.send_keys("Notebook")
search_box.send_keys(Keys.RETURN)

time.sleep(2)

botao = navegador.find_element(By.XPATH, "/html/body/div[2]/div[2]/a[1]")
botao.click()

time.sleep(10)

precos = []

try:
    preco_element = driver.find_element(By.CLASS_NAME, "sc-e5003a21-2 jfrbst priceCard")
    print(preco_element.text)
except Exception as e:
    print(f"Erro ao encontrar o elemento: {e}")


with open("prices.txt", "w") as file:
    for price in precos:
        file.write(price + "\n")

driver.quit()







