from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://rpachallenge.com/")

import pandas as pd

x = pd.read_excel(r"C:\Users\Luan\Downloads\challenge.xlsx", engine='openpyxl')

def fill_in_fields(ng_reflect_name, dado):
  driver.find_element(By.XPATH, (f"//input[@ng-reflect-name='{ng_reflect_name}']")).send_keys(dado)

driver.find_element(By.XPATH, ("//button[.='Start']")).click()

rounds = 0
while rounds < 11:

  primeiro_nome = x.loc[rounds]['First Name']
  ultimo_nome = x.loc[rounds]['Last Name ']
  nome_empresa = x.loc[rounds]['Company Name']
  cargo = x.loc[rounds]['Role in Company']
  endereco = x.loc[rounds]['Address']
  email = x.loc[rounds]['Email']
  numero_telefone = x.loc[rounds]['Phone Number']

  fill_in_fields('labelFirstName', primeiro_nome)
  fill_in_fields('labelLastName', ultimo_nome)
  fill_in_fields('labelCompanyName', nome_empresa)
  fill_in_fields('labelRole', cargo)
  fill_in_fields('labelAddress', endereco)
  fill_in_fields('labelEmail', email)
  fill_in_fields('labelPhone', str(numero_telefone))

  time.sleep(0.5)

  driver.find_element(By.XPATH, ("//input[@value='Submit']")).click()

  rounds = rounds + 1
  
  
        



#  driver.find_element(By.ID_NAME, "input").send_keys("TESTE PYTHON" + Keys.ENTER)
# def preenche_dados(campo, dado):
# "//input[@ng-reflect-name='labelFirstName']"
# Xpath =//tagname[@Attribute='value']


#   def preenche_dados(campo, dado):
#     for(rounds = 0; )
    

# print('Deu Certo!')