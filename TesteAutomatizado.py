from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

identificacao = [
    '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input', #nome
    '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input', #sobrenome
    '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input', #data nascimento
    '//*[@id="root"]/div/div/div[1]/div[2]/label[4]/input'  #cpf
]
contato = [
    '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input', #email
    '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input', #telefone 1
    '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input'  #telefone 2
]
endereco = [
    '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input', #logradouro
    '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input', #numero
    '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input', #bairro
    '//*[@id="root"]/div/div/div[1]/div[2]/label[4]/input', #cep
    '//*[@id="root"]/div/div/div[1]/div[2]/label[5]/input', #cidade
    '//*[@id="root"]/div/div/div[1]/div[2]/label[6]/select' #uf
]
usuario = [
    '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input', #nome
    '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input', #senha
    '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input'  #conformar senha
]
carteira = [
    '//*[@id="root"]/div/div/div[1]/div[2]/form/label[3]', #boleto
    '//*[@id="root"]/div/div/div[1]/div[2]/form/label[4]/input' #pix
]
proximo = '//*[@id="root"]/div/div/div[2]/div/div[2]/div/button'


navegador.get('http://localhost:3000')

#-- Teste area de identificação 
#Nome 
navegador.find_element('xpath', identificacao[0]).send_keys('Mario')
#Sobrenome
navegador.find_element('xpath', identificacao[1]).send_keys('Da Silva Melo')
#Data Nascimento
navegador.find_element('xpath', identificacao[2]).send_keys('15052023')
#CPF
navegador.find_element('xpath', identificacao[3]).send_keys('08777777777')
#Botão Proximo
navegador.find_element('xpath', proximo).click() 

time.sleep(2)

#-- Teste area de Contato  
#Email 
navegador.find_element('xpath', contato[0]).send_keys('mario@gmail.com')
#Telefone1  
navegador.find_element('xpath', contato[1]).send_keys('43999999999')
#Telefone2  
navegador.find_element('xpath', contato[2]).send_keys('43999997777')
#Botão Proximo
navegador.find_element('xpath', proximo).click() 

time.sleep(2)

#-- Teste area de Endereço  
#Logradouro 
navegador.find_element('xpath', endereco[0]).send_keys('Rua Leonor Fraga Furlan')
#Número  
navegador.find_element('xpath', endereco[1]).send_keys('37')
#Bairro  
navegador.find_element('xpath', endereco[2]).send_keys('Birro Luigi Amoreze')
#CEP
navegador.find_element('xpath', endereco[3]).send_keys('47850059')
#Cidade
navegador.find_element('xpath', endereco[4]).send_keys('Londrina')
#UF
navegador.find_element('xpath', endereco[5]).send_keys('Párana')
#Botão Proximo
navegador.find_element('xpath', proximo).click() 

time.sleep(2)

#-- Teste area de Usuário  
#Nome/Apelido 
navegador.find_element('xpath', usuario[0]).send_keys('Mario_02')
#Senha 
navegador.find_element('xpath', usuario[1]).send_keys('0@#rBdr')
#Confirmar Senha  
navegador.find_element('xpath', usuario[2]).send_keys('0@#rBdr')
#Botão Proximo
navegador.find_element('xpath', proximo).click() 

#-- Teste area de Carteira  
#Boleto 
navegador.find_element('xpath', carteira[0]).click() 
#Pix 
navegador.find_element('xpath', carteira[1]).click() 
#Botão Proximo
navegador.find_element('xpath', proximo).click() 
