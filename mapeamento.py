class Mapeamento:
    def __init__(self):
        self.emailChave = '//*[@id="root"]/div/div/div/div[2]/label[1]/input'
        self.emailValor = 'mario@gmail.com'
        self.senhaChave = '//*[@id="root"]/div/div/div/div[2]/label[2]/input'
        self.senhaValor = '@#1$bFs8'
        self.btn = '//*[@id="root"]/div/div/div/div[2]/button'

        self.cadastre_se = {
            '//*[@id="root"]/div/div/div/div[2]/a[1]': ''
        }
        self.formularioIdentificacao = {
            '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input': 'Mario',  
            '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input': 'Da Silva Melo', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input': '15052023', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[4]/input': '08777777777'  
        }
        self.formularioContato = {
            '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input': 'mario@gmail.com', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input': '43999999999', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input': ''  
        }
        self.forumularioEndereco = {
            '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input': 'Rua Leonor Fraga Furlan', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input': '37', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input': 'Bairro Luigi Amoreze', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[4]/input': '47850059', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[5]/input': 'Londrina',
            '//*[@id="root"]/div/div/div[1]/div[2]/label[6]/select': 'Párana' 
        }
        self.forumularioUsuario = {
            '//*[@id="root"]/div/div/div[1]/div[2]/label[1]/input': 'Mario_02', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[2]/input': '@#1$bFs8', 
            '//*[@id="root"]/div/div/div[1]/div[2]/label[3]/input': '@#1$bFs8'  
        }
        self.formularioCarteira = {
            '//*[@id="root"]/div/div/div[1]/div[2]/form/label[3]': '', 
            '//*[@id="root"]/div/div/div[1]/div[2]/form/label[4]/input': ''
        }
        self.confirmar = {
            '//*[@id="root"]/div/div/div[2]/div/div[2]/div/button': ''
        }

        self.proximo = '//*[@id="root"]/div/div/div[2]/div/div[2]/div/button'


    def getCadastro(self):
        cadastro = [
            self.cadastre_se,
            self.formularioIdentificacao, 
            self.formularioContato, 
            self.forumularioEndereco, 
            self.forumularioUsuario,
            self.formularioCarteira,
            self.confirmar
        ]

        return cadastro
    

    def getProximo(self):
        return self.proximo