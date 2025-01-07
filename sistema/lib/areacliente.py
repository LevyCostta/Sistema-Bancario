from conta import *

ARQUIVO_CONTAS = 'Sistema-Bancario/sistema/contas.json'

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

def depositar(contas, nome_cliente):
    numero_agencia = input('Digite o número da agência para depósito: ')
    numero_conta = int(input('Digite o número da conta para depósito: '))
    valor_deposito = float(input('Digite o valor que deseja depositar: '))
    
    for conta in contas:
        if conta['Titular'] == nome_cliente and conta['Número'] == numero_conta and conta['Agência'] == numero_agencia:
            if valor_deposito > 0:
                conta['Saldo'] += valor_deposito
                salvar_dadoscontas(contas)
                print(f'Depósito de R${valor_deposito} realizado com sucesso! Novo saldo: R${conta["Saldo"]}.')
                return
            else:
                print('O valor do depósito deve ser positivo.')
                return
    print('Conta ou agência não encontrada, ou não pertence ao cliente.')

def sacar(contas, nome_cliente):
    numero_agencia = input('Digite o número da agência para saque: ')
    numero_conta = int(input('Digite o número da conta para saque: '))
    valor_saque = float(input('Digite o valor que deseja sacar: '))
    
    for conta in contas:
        if conta['Titular'] == nome_cliente and conta['Número'] == numero_conta and conta['Agência'] == numero_agencia:
            if conta['Saldo'] >= valor_saque:
                conta['Saldo'] -= valor_saque
                salvar_dadoscontas(contas)
                print(f'Saque de R${valor_saque} realizado com sucesso! Novo saldo: R${conta["Saldo"]}.')
                return
            else:
                print('Saldo insuficiente para realizar o saque.')
                return
    print('Conta ou Agência não encontrada, ou não pertence ao cliente.')

def menu_areacliente():
    contas = carregar_dadoscontas()
    nome_cliente = input('Digite o nome do cliente para iniciar: ').title()
    while True:
        cabecalho('ACESSO DO CLIENTE'.center(50))
        resposta = menu(['Listar Minhas Contas Bancárias', 'Depositar', 'Sacar', 'Sair'])
        if resposta == 1:
            listar_contas_cliente(contas, nome_cliente)
        elif resposta == 2:
            depositar(contas, nome_cliente)
        elif resposta == 3:
            sacar(contas, nome_cliente)
        elif resposta ==4:
            break
