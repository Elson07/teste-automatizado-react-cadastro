from testeAutomatizado import TesteAutomatizado
from time import sleep
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

    if opcao == '1': 
        navegador = TesteAutomatizado()
        navegador.cadastroSucesso(0.5)
    elif opcao == '2':
        navegador = TesteAutomatizado()
        navegador.login(0.5)

    
menu()

sleep(5)
print('\n'*4)
cont = input('Deseja realizar mais alguma operação? [S/N]: ')
print(cont)
print('\n'*4)
