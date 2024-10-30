from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar o WebDriver
opts = ChromeOptions()
opts.add_experimental_option("detach", True)  # Manter o navegador aberto após execução
navegador = webdriver.Chrome(options=opts)

# Acessar o site da Kabum
url = 'https://www.kabum.com.br/'
navegador.get(url)

# Aceitar cookies
botao_cookies = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
)
botao_cookies.click()

# Pesquisar por "notebook"
search_box = navegador.find_element(By.TAG_NAME, "input")
search_box.clear()
search_box.send_keys("Notebook")
search_box.send_keys(Keys.RETURN)

# Aguardar os resultados carregarem
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "product-card"))
)

# Encontrar os preços dos notebooks
precos = []
preco_elements = navegador.find_elements(By.CLASS_NAME, "price")  # Ajuste a classe conforme necessário

for preco in preco_elements[:3]:  # Pegar apenas os três primeiros preços
    precos.append(preco.text)

# Exibir os preços encontrados
print("Preços encontrados:", precos)

# Fechar o navegador
navegador.quit()