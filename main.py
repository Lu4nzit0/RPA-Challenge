from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os.path
import os

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://rpachallenge.com/")


def download():
  driver.find_element(By.XPATH, (f"//a[@href='./assets/downloadFiles/challenge.xlsx']")).click()


if os.path.exists(r'C:\Users\Luan\Downloads\challenge.xlsx'):
  print("O arquivo já existe!")
  os.remove(r'C:\Users\Luan\Downloads\challenge.xlsx')
  download()
  
else:
  print("O arquivo não existe!")
  print("Realizando download..")
  download() 

def fill_in_fields(ng_reflect_name, dado):
  driver.find_element(By.XPATH, (f"//input[@ng-reflect-name='{ng_reflect_name}']")).send_keys(dado)

driver.find_element(By.XPATH, ("//button[.='Start']")).click()

x = pd.read_excel(r'C:\Users\Luan\Downloads\challenge.xlsx', engine='openpyxl')
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

  driver.find_element(By.XPATH, ("//input[@value='Submit']")).click()

  rounds = rounds + 1    
 

# "//input[@ng-reflect-name='labelFirstName']"
# Xpath =//tagname[@Attribute='value']


