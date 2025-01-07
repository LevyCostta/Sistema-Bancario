from time import sleep
import json
import os
from utilidades import *
from agencia import Agencia

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.agencias = []

    def adicionar_agencia(self, agencia):
        self.agencias.append(agencia)

# Nome do arquivo onde os dados serão salvos
ARQUIVO_BANCOS = 'bancos.json'

# Função para carregar os dados do arquivo JSON
def carregar_dadosbanco():
    if os.path.exists(ARQUIVO_BANCOS):
        with open(ARQUIVO_BANCOS, 'r') as arquivo:
            return json.load(arquivo)
    return []

# Função para salvar os dados no arquivo JSON
def salvar_dadosbancos(bancos):
    with open(ARQUIVO_BANCOS, 'w') as arquivo:
        json.dump(bancos, arquivo, indent=4)

# Função para verificar se já existe um banco cadastrado com o nome/agência digitado
def banco_existe(bancos, nome=None, agencia=None):
    for banco in bancos:
        if nome and banco['nome'] == nome:
            return True
        if agencia:
            for ag in banco['agencias']:
                if ag['numero'] == agencia:
                    return True
    return False


# Cadastro de Bancos
def cadastrar_banco(bancos):
    # NOME DO BANCO
    while True:
        nome = input('Digite o nome do banco a ser registrado no sistema: ').title()
        if banco_existe(bancos, nome=nome):
            print(f'\nO banco {nome} já está registrado no nosso sistema.\n')
            sleep(2)
            return
        elif nome == "":
            print('\n*** Nome não pode ser vazio ***')
        elif len(nome) < 2:
            print('Nome muito curto, digite outro com pelo menos 2 caracteres\n')
        else:
            break

    banco = Banco(nome)

    # Adiciona o banco como dicionário diretamente
    bancos.append({"nome": banco.nome, "agencias": []})
    salvar_dadosbancos(bancos)
    print('\nBanco Cadastrado com Sucesso!')
    sleep(2)

# LISTAR BANCOS CADASTRADOS
def listar_bancos(bancos):
    if not bancos:
        print('Nenhum Banco Cadastrado.')
    else:
        for banco in bancos:
            agencias = ", ".join(agencia['numero'] for agencia in banco['agencias'])
            print(f'Banco: {banco["nome"]}, Agências: {agencias}')
    sleep(2)

# PESQUISAR UM BANCO JÁ REGISTRADO
def pesquisar_banco(bancos):
    nome = input('Digite o nome do banco para pesquisar: ').title()
    for banco in bancos:
        if banco['nome'] == nome:
            agencias = ", ".join(agencia['numero'] for agencia in banco['agencias'])
            print(f'Banco encontrado: {banco["nome"]}, Agências: {agencias}')
            return
    print('Banco não encontrado.')
    sleep(2)

# EXCLUIR UM BANCO
def excluir_banco(bancos):
    nome = input('Digite o nome do banco a ser excluído: ').title()
    for banco in bancos:
        if banco['nome'] == nome:
            bancos.remove(banco)
            salvar_dadosbancos(bancos)
            print(f'Banco {nome} excluído com sucesso!')
            return
    print('Banco não encontrado.')
    sleep(2)

# Menu de Gerenciamento de Bancos
def menu_bancos():
    bancos = carregar_dadosbanco()
    while True:
        cabecalho ('GERENCIAR BANCOS'.center(50))
        resposta = menu(['Novo Banco', 'Listar Bancos', 'Pesquisar Banco', 'Excluir Banco', 'Voltar ao Menu Anterior'])
        if resposta == 1:
            cadastrar_banco(bancos)
        elif resposta == 2:
            listar_bancos(bancos)
        elif resposta == 3:
            pesquisar_banco(bancos)
        elif resposta == 4:
            excluir_banco(bancos)
        elif resposta == 5:
            break
        else:
            print('ERRO - Digite uma opção válida!')
            sleep(2)
