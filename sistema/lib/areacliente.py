from conta import *

ARQUIVO_CONTAS = 'contas.json'

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

def listar_contas_cliente(contas, nome_cliente):
    contas_cliente = [conta for conta in contas if conta['Titular'] == nome_cliente]
    if not contas_cliente:
        print(f"Nenhuma conta encontrada para o cliente {nome_cliente}.")
    else:
        print(f"Contas do cliente {nome_cliente}:")
        for conta in contas_cliente:
            print(f"""Banco: {conta["Banco"]}
Número: {conta["Número"]}
Agência: {conta["Agência"]}
Saldo: R${conta["Saldo"]}""")
            linha()

def menu_areacliente():
    contas = carregar_dadoscontas()
    nome_cliente = input('Digite o nome do cliente para iniciar: ').title()
    while True:
        cabecalho('ACESSO DO CLIENTE'.center(50))
        resposta = menu(['Listar Minhas Contas Bancárias', 'Sair'])
        if resposta == 1:
            listar_contas_cliente(contas, nome_cliente)
        elif resposta == 2:
            print("Saindo...")
            break


menu_areacliente()