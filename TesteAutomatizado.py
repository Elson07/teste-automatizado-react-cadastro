from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from time import sleep
from mapeamento import Mapeamento

class TesteAutomatizado(Mapeamento):
    
    def __init__(self):
        super().__init__()
        self.chrome_service = Service(ChromeDriverManager().install())
        self.chrome_options = ChromeOptions()    
        self.chrome_options.add_experimental_option("detach", True) 
        self.navegador = webdriver.Chrome(options=self.chrome_options, service=self.chrome_service) 
        self.navegador.get('http://localhost:3000')
        self.navegador.maximize_window()
    

    def login(self, transicao):
        self.navegador.find_element('xpath', self.emailChave).send_keys(self.emailValor)
        sleep(transicao)
        self.navegador.find_element('xpath', self.senhaChave).send_keys(self.senhaValor)
        sleep(transicao)
        self.navegador.find_element('xpath', self.btn).click()


    def cadastroSucesso(self, transicao):
        for formulario in self.getCadastro():
            for chave, valor in formulario.items():
                if valor != '': 
                    sleep(transicao)
                    self.navegador.find_element('xpath', chave).send_keys(valor)
                else:
                    sleep(transicao)
                    self.navegador.find_element('xpath', chave).click()
            self.navegador.find_element('xpath', self.getProximo()).click() 
        self.navegador.keyDown('Home')
