from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from time import sleep

class TesteAutomatizado:
    
    def __init__(self):
        self.chrome_service = Service(ChromeDriverManager().install()) #Instala a versão mais recente do drive
        self.chrome_options = ChromeOptions()    #Permite configurar o driver do chrome
        self.chrome_options.add_experimental_option("detach", True) #Este metodo impede que o navegador seja fechado apos o fim das intruções
        self.navegador = webdriver.Chrome(options=self.chrome_options, service=self.chrome_service) #Intancia um navegador
        self.navegador.get('http://localhost:3000')
        self.navegador.maximize_window()
    

    def login(self, transicao):
        self.navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[2]/label[1]/input').send_keys("mario@gmail.com")
        sleep(transicao)
        self.navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[2]/label[2]/input').send_keys("@#1$bFs8")
        sleep(transicao)
        self.navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[2]/button').click()


navegador = TesteAutomatizado()
navegador.login(0.5)


'''
    def cadastroSucesso(transicao):
        #Mapeamento dos formularios por xpath com valores injetado
        cadastre_se = {
            '//*[@id="root"]/div/div/div/div[2]/a[1]': ''
        }
        formularioIdentificacao = {
            '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input': 'Mario',  
            '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input': 'Da Silva Melo', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input': '15052023', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[4]/input': '08777777777'  
        }
        formularioContato = {
            '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input': 'mario@gmail.com', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input': '43999999999', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input': ''  
        }
        forumularioEndereco = {
            '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input': 'Rua Leonor Fraga Furlan', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input': '37', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input': 'Bairro Luigi Amoreze', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[4]/input': '47850059', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[5]/input': 'Londrina',
            '//*[@id="root"]/div/div/div[1]/div[2]/label[6]/select': 'Párana' 
        }
        forumularioUsuario = {
            '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input': 'Mario_02', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input': '@#1$bFs8', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input': '@#1$bFs8'  
        }
        formularioCarteira = {
            '//*[@id="root"]/div/div/div[1]/div[2]/form/label[3]': '', 
            '//*[@id="root"]/div/div/div[1]/div[2]/form/label[4]/input': ''
        }
        confirmar = {
            '//*[@id="root"]/div/div/div[2]/div/div[2]/div/button': ''
        }
        cadastro = [
            cadastre_se,
            formularioIdentificacao, 
            formularioContato, 
            forumularioEndereco, 
            forumularioUsuario,
            formularioCarteira,
            confirmar
        ]
        proximo = '//*[@id="root"]/div/div/div[2]/div/div[2]/div/button'
        for formulario in cadastro:
            for chave, valor in formulario.items():
                if valor != '': 
                    sleep(transicao)
                    navegador.find_element('xpath', chave).send_keys(valor)
                else:
                    sleep(transicao)
                    navegador.find_element('xpath', chave).click()
            navegador.find_element('xpath', proximo).click() 
        navegador.keyDown('Home')


    def login(transicao):
        navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[2]/label[1]/input').send_keys("mario@gmail.com")
        sleep(transicao)
        navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[2]/label[2]/input').send_keys("@#1$bFs8")
        sleep(transicao)
        navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[2]/button').click()



    def menu(): 
        print("\n"*6)
        print(' {}'.format('_'*60))
        print('|{0:^60}|'.format('Programa de testes de casos de uso'))
        print('|{}|'.format('-'*60))
        print('|{0:<60}|'.format(' Escolha uma das opções')) 
        print('|{}|'.format('-'*60))
        print('|{0:<60}|'.format('[1] Cadastro de úsuario'))
        print('|{0:<60}|'.format('[2] Login'))
        print('|{0:<60}|'.format('[3] Deletar usuario do Firebase'))
        print('|{}|'.format('_'*60))
        opcao = input('')

        if opcao == 1: 
            cadastroSucesso(0.1)
        elif opcao == 2:
            login()


    #cadastroSucesso(0.2)
    login(0.2)


'''