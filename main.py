from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://rpachallenge.com/")

import pandas as pd

x = pd.read_excel(r"C:\Users\Luan\Downloads\challenge.xlsx", engine='openpyxl')

primeiro_nome = x.loc[0]['First Name']
ultimo_nome = x.loc[0]['Last Name ']
nome_empresa = x.loc[0]['Company Name']
cargo = x.loc[0]['Role in Company']
endereco = x.loc[0]['Address']
email = x.loc[0]['Email']
numero_telefone = x.loc[0]['Phone Number']



driver.find_element(By.XPATH, ("//input[@ng-reflect-name='labelFirstName']")).send_keys("Luan")

#  driver.find_element(By.ID_NAME, "input").send_keys("TESTE PYTHON" + Keys.ENTER)
# def preenche_dados(campo, dado):
# "//input[@ng-reflect-name='labelFirstName']"
# Xpath =//tagname[@Attribute='value']


  def preenche_dados(campo, dado):
    for(rounds = 0; )
    

print('Deu Certo!')