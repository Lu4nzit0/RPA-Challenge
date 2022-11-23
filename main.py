from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://rpachallenge.com/")

import pandas as pd

x = pd.read_excel(r"C:\Users\Luan\Downloads\challenge.xlsx", engine='openpyxl')

def preenche_dados(ng_reflect_name, dado):
  driver.find_element(By.XPATH, (f"//input[@ng-reflect-name='{ng_reflect_name}']")).send_keys(dado)

driver.find_element(By.XPATH, ("//button[.='Start']")).click()

repeticao = 0
while repeticao < 11:

  primeiro_nome = x.loc[repeticao]['First Name']
  ultimo_nome = x.loc[repeticao]['Last Name ']
  nome_empresa = x.loc[repeticao]['Company Name']
  cargo = x.loc[repeticao]['Role in Company']
  endereco = x.loc[repeticao]['Address']
  email = x.loc[repeticao]['Email']
  numero_telefone = x.loc[repeticao]['Phone Number']


  preenche_dados('labelFirstName', primeiro_nome)
  preenche_dados('labelLastName', ultimo_nome)
  preenche_dados('labelCompanyName', nome_empresa)
  preenche_dados('labelRole', cargo)
  preenche_dados('labelAddress', endereco)
  preenche_dados('labelEmail', email)
  preenche_dados('labelPhone', str(numero_telefone))

  time.sleep(0.2)

  driver.find_element(By.XPATH, ("//input[@value='Submit']")).click()

  repeticao = repeticao + 1
  
  
        



#  driver.find_element(By.ID_NAME, "input").send_keys("TESTE PYTHON" + Keys.ENTER)
# def preenche_dados(campo, dado):
# "//input[@ng-reflect-name='labelFirstName']"
# Xpath =//tagname[@Attribute='value']


#   def preenche_dados(campo, dado):
#     for(rounds = 0; )
    

# print('Deu Certo!')