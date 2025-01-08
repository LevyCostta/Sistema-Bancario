# main.py
from time import sleep
import json
import os
from utilidades import *
from pessoa import *
from banco import *
from agencia import *
from datetime import datetime

ARQUIVO_CONTAS = 'Sistema-Bancario/sistema/contas.json'

def carregar_dadoscontas():
    if os.path.exists(ARQUIVO_CONTAS):
        with open(ARQUIVO_CONTAS, 'r') as arquivo:
            contas = json.load(arquivo)
            # Garantir que cada conta tenha um extrato
            for conta in contas:
                if 'extrato' not in conta:
                    conta['extrato'] = []  # Inicializa o extrato como uma lista vazia
            return contas
    return []

def salvar_dadoscontas(contas):
    with open(ARQUIVO_CONTAS, 'w') as arquivo:
        json.dump(contas, arquivo, indent=4)

def conta_existe(contas, numero_conta):
    for conta in contas:
        if conta['Número'] == numero_conta:
            return True
    return False

class Conta:
    def __init__(self, nome, cpf, numero, agencia, banco, saldo=0):
        self.nome = nome
        self.cpf = cpf #MUDAR PARA ADICIONAR A CLASSE CLIENTE, SUBSTITUIR NOME E CPF
        self.numero = numero
        self.agencia = agencia
        self.banco = banco
        self.saldo = saldo
        self.extrato = []

# FUNÇÃO PARA CADASTRAR NOVOS CLIENTES (JÁ CADASTRADOS NA CLASSE PESSOA)
def cadastrar_conta(contas):
    bancos = carregar_dadosbanco()
    nome_banco = input('Digite o nome do banco ao qual o cliente será cadastrado: ').title()
    
    banco_encontrado = next((banco for banco in bancos if banco['nome'] == nome_banco), None)
    if banco_encontrado is None:
        print('Banco não encontrado.')
        sleep(2)
        return  
    pessoas = carregar_dadospessoa()
    while True:
        nome = input('Digite o nome da pessoa que deseja como mais novo Cliente: ').title()
        if titular_existe(pessoas, nome):
            cpf = input('Digite o CPF da pessoa que deseja como mais novo Cliente: ')
            if titular_existe(pessoas, cpf=cpf):
                numero_agencia = input('Digite o número da agência: ')
                if agencia_existe(bancos, numero_agencia):
                    numero_conta = int(input('Digite o número da conta: '))
                    if conta_existe(contas, numero_conta):
                        print('Conta já cadastrada!')
                        continue
                else:
                    print(f'Agência {numero_agencia} não encontrada!')
                    continue
            else:
                print('Pessoa não cadastrada com este CPF! Cadastre a pessoa antes de criar a conta Cliente.')
                return
                
            conta = Conta(nome, cpf, numero_conta, numero_agencia, nome_banco)  # Adicionando o banco
            contas.append({
                "Titular": conta.nome,
                "CPF": conta.cpf,
                "Número": conta.numero,
                "Agência": conta.agencia,
                "Banco": conta.banco,
                "Saldo": conta.saldo
            })
            salvar_dadoscontas(contas)
            print('Cliente Cadastrado com sucesso!')
            break

        else:
            print('Pessoa não cadastrada! Cadastre a pessoa antes de criar a conta Cliente.')
            return

# FUNÇÃO PARA LISTAR CONTAS CADASTRADAS
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("Lista de Contas:")
        for conta in contas:
            print(f"""Titular: {conta["Titular"]}
CPF: {conta["CPF"]}
Banco: {conta["Banco"]}
Número: {conta["Número"]}
Agência: {conta["Agência"]}
Saldo: R${conta["Saldo"]}""")
            linha()

# PESQUISAR CONTAS CADASTRADAS
def pesquisar_conta(contas):
    nome = input('Digite o nome do Cliente que deseja buscar: ').title()      
    for conta in contas:
        if conta['Titular'] == nome:
            print('CONTA ENCONTRADA, CARREGANDO...')
            print('')
            print('-' * 50)
            sleep(2)
            print(f'Titular: {conta["Titular"]}, CPF: {conta["CPF"]}, Banco: {conta["Banco"]}, Número: {conta["Número"]}, Agência: {conta["Agência"]}')
            return
    print('Conta Não Encontrada!')

# FUNÇÃO PARA EXCLUIR CONTA CLIENTE
def excluir_conta(contas):
    cpf = input('Digite o CPF da conta a ser excluída: ')
    for conta in contas:
        if conta['CPF'] == cpf:
            contas.remove(conta)
            salvar_dadoscontas(contas)
            print(f'Conta com o CPF: {cpf}, foi excluída.')
            return
    print('Conta não encontrada')
    sleep(2)

# MENU PARA CHAMAR A CLASSE CONTA
def menu_contas():
    contas = carregar_dadoscontas()
    while True:
        cabecalho('GERENCIAR CONTAS'.center(50))
        resposta = menu(['Nova Conta', 'Listar Contas', 'Pesquisar Conta', 'Excluir Conta', 'Voltar ao Menu Anterior'])
        if resposta == 1:
            cadastrar_conta(contas)
        elif resposta == 2:
            listar_contas(contas)
            sleep(2)
        elif resposta == 3:
            pesquisar_conta(contas)
        elif resposta == 4:
            excluir_conta(contas)
        elif resposta == 5:
            break
        else:
            print('ERRO - Digite uma opção válida!')
            sleep(2)
