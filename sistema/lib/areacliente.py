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
    valor_deposito = float(input('Digite o valor que deseja depositar: ').replace(",", "."))
    
    for conta in contas:
        if conta['Titular'] == nome_cliente and conta['Número'] == numero_conta and conta['Agência'] == numero_agencia:
            if valor_deposito > 0:
                conta['Saldo'] += valor_deposito
                #ADICIONA DEPOSITO AO EXTRATO
                conta['extrato'].append({
                    'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                    'tipo': 'Depósito',
                    'valor': valor_deposito
                })
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
    valor_saque = float(input('Digite o valor que deseja sacar: ').replace(",", "."))
    
    for conta in contas:
        if conta['Titular'] == nome_cliente and conta['Número'] == numero_conta and conta['Agência'] == numero_agencia:
            if conta['Saldo'] >= valor_saque:
                conta['Saldo'] -= valor_saque
                # Adiciona a transação ao extrato
                conta['extrato'].append({
                    'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                    'tipo': 'Saque',
                    'valor': valor_saque
                })
                salvar_dadoscontas(contas)
                print(f'Saque de R${valor_saque} realizado com sucesso! Novo saldo: R${conta["Saldo"]}.')
                return
            else:
                print('Saldo insuficiente para realizar o saque.')
                return
    print('Conta ou Agência não encontrada, ou não pertence ao cliente.')

def transferir(contas, nome_cliente):
    numero_agencia_remetente = input('Digite o número da agência do remetente: ')
    numero_conta_remetente = int(input('Digite o número da conta do remetente: '))
    print('\nAgora vamos precisar dos dados da conta do destinatário:')
    sleep(2)
    
    numero_agencia_destinatario = input('\nDigite o número da agência do destinatário: ')
    numero_conta_destinatario = int(input('Digite o número da conta do destinatário: '))
    valor_transferencia = float(input('Digite o valor que deseja transferir: ').replace(",", "."))
    
    conta_remetente = None
    conta_destinatario = None

    for conta in contas:
        if conta['Titular'] == nome_cliente and conta['Número'] == numero_conta_remetente and conta['Agência'] == numero_agencia_remetente:
            conta_remetente = conta
        if conta['Número'] == numero_conta_destinatario and conta['Agência'] == numero_agencia_destinatario:
            conta_destinatario = conta

    if conta_remetente and conta_destinatario:
        if conta_remetente['Saldo'] >= valor_transferencia:
            conta_remetente['Saldo'] -= valor_transferencia
            conta_destinatario['Saldo'] += valor_transferencia
            # Adiciona a transação ao extrato
            conta_remetente['extrato'].append({
                'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'tipo': 'Transferência Enviada',
                'valor': valor_transferencia
            })
            conta_destinatario['extrato'].append({
                'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'tipo': 'Transferência Recebida',
                'valor': valor_transferencia
            })
            salvar_dadoscontas(contas)
            print(f'Transferência de R${valor_transferencia} realizada com sucesso!')
            print(f'Novo saldo em conta: R${conta_remetente["Saldo"]}.')
            
        else:
            print('Saldo insuficiente para realizar a transferência.')
    else:
        print('Conta do remetente ou destinatário não encontrada.')

def extrato(contas, nome_cliente):
    numero_agencia = input('Digite o número da agência para visualizar o extrato: ')
    numero_conta = int(input('Digite o número da conta para visualizar o extrato: '))
    
    for conta in contas:
        if conta['Titular'] == nome_cliente and conta['Número'] == numero_conta and conta['Agência'] == numero_agencia:
            linha()
            print(f'Extrato Bancario'.center(50))
            linha()
            print(f'Cliente: {conta['Titular']}')
            print(f'Banco: {conta['Banco']}')
            print(f'Conta: {conta['Número']}')
            print(f'Agência: {conta['Agência']}')
            linha()
            print('Histórico de Transações'.center(50))
            linha()
            if not conta['extrato']:
                print("Nenhuma transação registrada.")
            else:
                for transacao in conta['extrato']:
                    print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']:.2f}")
            linha()
            print(f"Saldo Atual: R${conta['Saldo']:.2f}")
            linha()
            return
    print('Conta ou Agência não encontrada, ou não pertence ao cliente.')

def menu_areacliente():
    contas = carregar_dadoscontas()
    nome_cliente = input('Digite o nome do cliente para iniciar: ').title()
    while True:
        cabecalho('ACESSO DO CLIENTE'.center(50))
        resposta = menu(['Listar Minhas Contas Bancárias', 'Depositar', 'Sacar', 'Efetuar Transferência', 'Obter Extrato', 'Voltar ao Menu Anterior'])
        if resposta == 1:
            listar_contas_cliente(contas, nome_cliente)
        elif resposta == 2:
            depositar(contas, nome_cliente)
        elif resposta == 3:
            sacar(contas, nome_cliente)
        elif resposta == 4:
            transferir(contas, nome_cliente)
        elif resposta == 5:
            extrato(contas, nome_cliente)
        elif resposta == 6:
            break
        else:
            print('ERRO - Digite uma opção válida!')
            sleep(2)
