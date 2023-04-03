# Importação de módulos
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os

# Encerra todos os processos do navegador Chrome
# os.system("TASKKILL /f /IM CHROME.EXE")

# Realiza abertura do navegador Chrome.
driver = webdriver.Chrome()

# Aguarda carregamento dos elementos utilizados no desafio.
driver.implicitly_wait(10)

# Abertura do site do desafio.
driver.get("https://rpachallenge.com/")

# Função que localiza e clica no botão de Download.
def download():
  driver.find_element(By.XPATH, (f"//a[@href='./assets/downloadFiles/challenge.xlsx']")).click()

# Função que aguarda a finalização do download realizado.
def waitDownloadFile(caminho):
  while not os.path.exists(caminho):
    time.sleep(1)

# Variável contendo o caminho de armazenamento do download realizado.
# caminho_do_arquivo = r'C:\Users\Luan\Downloads\challenge.xlsx'
caminho_do_arquivo = os.path.expanduser("~")+"\Downloads\challenge.xlsx"

# Verifica existência do arquivo no diretório, caso o mesmo já exista é realizado a remoção e feito um novo download.
if os.path.exists(caminho_do_arquivo):
  print("O arquivo já existe!")
  # os.remove(caminho_do_arquivo)
  download()

# Caso o arquivo não exista no diretório é realizado o download do mesmo.
else:
  print("O arquivo não existe!")
  print("Realizando download..")
  download() 

# Parametrização de função que realiza a localiza e preenche os campos corretamente.
def fill_in_fields(ng_reflect_name, dado):
  driver.find_element(By.XPATH, (f"//input[@ng-reflect-name='{ng_reflect_name}']")).send_keys(dado)

# Localiza e clica no botão de contagem dos rounds
driver.find_element(By.XPATH, ("//button[.='Start']")).click()

# Chamada de função que aguarda finalização do donwload realizado.
waitDownloadFile(caminho_do_arquivo)

x = pd.read_excel(caminho_do_arquivo, engine='openpyxl')
rounds = 0

while rounds < 10:
  
  # Acessa linhas e colunas da planilha baixada
  primeiro_nome = x.loc[rounds]['First Name']
  ultimo_nome = x.loc[rounds]['Last Name ']
  nome_empresa = x.loc[rounds]['Company Name']
  cargo = x.loc[rounds]['Role in Company']
  endereco = x.loc[rounds]['Address']
  email = x.loc[rounds]['Email']
  numero_telefone = x.loc[rounds]['Phone Number']

# Localiza e preenche os campos corretamente com o dado solicitado
  fill_in_fields('labelFirstName', primeiro_nome)
  fill_in_fields('labelLastName', ultimo_nome)
  fill_in_fields('labelCompanyName', nome_empresa)
  fill_in_fields('labelRole', cargo)
  fill_in_fields('labelAddress', endereco)
  fill_in_fields('labelEmail', email)
  fill_in_fields('labelPhone', str(numero_telefone))  

  driver.find_element(By.XPATH, ("//input[@value='Submit']")).click()

  rounds = rounds + 1 