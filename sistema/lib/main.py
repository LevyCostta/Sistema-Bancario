from utilidades import *
from pessoa import *
from banco import *
from agencia import *
from conta import *
from areacliente import *

def main_menu():
    while True:
        cabecalho('SISTEMA BANCARIO')
        resposta = menu(['Administrar o Sistema','Acessar como Cliente','Sair'])
        if resposta == 1:
            main()
        elif resposta == 2:
            menu_areacliente()
        else:
            print('ERRO - Digite uma opção válida!')
            sleep(2)

def main():
    while True:
        cabecalho('MENU PRINCIPAL'.center(50))
        resposta = menu(['Gerenciar Bancos', 'Gerenciar Agências','Gerenciar Pessoas','Gerenciar Contas','Voltar ao Menu Anterior'])
        if resposta == 1:
            menu_bancos()
        elif resposta == 2:
            menu_agencias()
        elif resposta == 3:
            menu_pessoas()
        elif resposta == 4:
            menu_contas()
        elif resposta == 5:
            main_menu()
        else:
            print('ERRO - Digite uma opção válida!')
            sleep(2)

main_menu()