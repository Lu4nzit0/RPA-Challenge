# Importação de módulos
# Import of modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os

# Encerra todos os processos do navegador Chrome
# Terminate all Chrome browser processes
os.system("TASKKILL /f /IM CHROME.EXE")

# Realiza abertura do navegador Chrome.
# Performs the opening of the Chrome browser.
driver = webdriver.Chrome()

# Configura o driver para aguardar até 10 segundos pelo surgimento dos elementos web utilizados.
# Configures the Driver to wait up to 10 secopnds for the web elements used to appear
driver.implicitly_wait(10)

# Abre o site do desafio.
# Open the challenge website.
driver.get("https://rpachallenge.com/")

# Função que localiza e clica no botão de Download.
# Function that locates and clicks the download button
def download():
  driver.find_element(By.XPATH, (f"//a[@href='./assets/downloadFiles/challenge.xlsx']")).click()

# Função que aguarda a finalização do download realizado.
# Function that waits for the completion of the download performed.
def waitDownloadFile(caminho):
  while not os.path.exists(caminho):
    time.sleep(1)

# Variável contendo o caminho de armazenamento do download realizado.
# Variable containing the storage path of the download.
caminho_do_arquivo = os.path.expanduser("~")+"\Downloads\challenge.xlsx"

# Verifica existência do arquivo no diretório. Caso o mesmo já exista, é realizado a remoção e feito um novo download.
# Checks the existence of the file in the directory. If it already exists, it is removed and a new download is made.
if os.path.exists(caminho_do_arquivo):
  print("O arquivo já existe!")
  os.remove(caminho_do_arquivo)
  download()

# Caso o arquivo não exista no diretório é realizado o download do mesmo.
# If the file does not exists in the directory, it is downloaded.
else:
  print("O arquivo não existe!\nRealizando download..")
  download() 

# Função que localiza e preenche os campos com os dados corretamente.
# Function that locates and fill in the fields correctly
def fill_in_fields(ng_reflect_name, dado):
  driver.find_element(By.XPATH, (f"//input[@ng-reflect-name='{ng_reflect_name}']")).send_keys(dado)

# Localiza e clica no botão de início do desafio.
# Locates and clicks in the start challenge button
driver.find_element(By.XPATH, ("//button[.='Start']")).click()

# Chamada de função que aguarda finalização do donwload realizado.
waitDownloadFile(caminho_do_arquivo)

# Leitura do arquivo XLSX.
# Read the file XLXS.
x = pd.read_excel(caminho_do_arquivo, engine='openpyxl')
rounds = 0

# Define repetições do preenchimento do formulário.
# Sets repetitions of filling ou the form.
while rounds < 10:
  
  # Define as variáveis com os dados da planilha.
  # Defines variables with the worksheet data.
  primeiro_nome = x.loc[rounds]['First Name']
  ultimo_nome = x.loc[rounds]['Last Name ']
  nome_empresa = x.loc[rounds]['Company Name']
  cargo = x.loc[rounds]['Role in Company']
  endereco = x.loc[rounds]['Address']
  email = x.loc[rounds]['Email']
  numero_telefone = x.loc[rounds]['Phone Number']

# Localiza e preenche os campos corretamente com o dado solicitado
# Locates and fills in the fields correctly with the requested data
  fill_in_fields('labelFirstName', primeiro_nome)
  fill_in_fields('labelLastName', ultimo_nome)
  fill_in_fields('labelCompanyName', nome_empresa)
  fill_in_fields('labelRole', cargo)
  fill_in_fields('labelAddress', endereco)
  fill_in_fields('labelEmail', email)
  fill_in_fields('labelPhone', str(numero_telefone))  

# Localiza e clica no botão de envio do formulário.
# Locates and click on the submit button
  driver.find_element(By.XPATH, ("//input[@value='Submit']")).click()

# Contagem de repetições
# Repetition counts
  rounds = rounds + 1 

# Aguarda 10 segundos
# Wait 10 seconds
time.sleep(10)

# Fecha o navegador
# Close the browser
driver.close()