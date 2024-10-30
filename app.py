from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
# Se estiver usando o Pycharm para desenvolvedor,
# Adicione estas linhas
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
# Passe a variavel opts para o webdriver
navegador = webdriver.Chrome(options=opts)
url = r'https://www.kabum.com.br/conectividade/dispositivo-de-rede/roteador'
navegador.get(url)

''' preco = navegador.find_element(By.XPATH, "/html/body/div/div[3]/h2")
#print(preco.text)'''

campo_nome = navegador.find_element(By.ID, "name")
campo_nome.send_keys("Paulo Brificado")
campo_mensagem = navegador.find_element(By.ID, "message")
campo_mensagem.send_keys("A Globo é um Lixo!")

botao = navegador.find_element(By.XPATH, "html/body/form/button")
botao.click()