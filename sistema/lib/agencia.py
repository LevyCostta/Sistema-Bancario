from time import sleep
import os
import json
from utilidades import *
from banco import *

# Nome do arquivo onde os dados serão salvos
ARQUIVO_BANCOS = 'bancos.json'

class Agencia:
    def __init__(self, numero):
        self.numero = numero

def carregar_dadosagencia():
    if os.path.exists(ARQUIVO_BANCOS):
        with open(ARQUIVO_BANCOS, 'r') as arquivo:
            return json.load(arquivo)
    return []

def salvar_dadosagencia(bancos):
    with open(ARQUIVO_BANCOS, 'w') as arquivo:
        json.dump(bancos, arquivo, indent=4)

def agencia_existe(bancos, numero_agencia):
    """Verifica se uma agência com o número especificado já existe em qualquer banco."""
    for banco in bancos:
        for agencia in banco['agencias']:
            if agencia['numero'] == numero_agencia:
                return True
    return False


def cadastrar_agencia(bancos):
    nome_banco = input('Digite o nome do banco para adicionar uma nova agência: ').title()
    
    banco_encontrado = next((banco for banco in bancos if banco['nome'] == nome_banco), None)
    if banco_encontrado is None:
        print('Banco não encontrado.')
        sleep(2)
        return

    while True:
        agencia_numero = input('Digite o número da nova agência: ')
        if not agencia_numero.isdigit() or len(agencia_numero) != 4:
            print('Digite uma agência válida (Apenas Números, exatamente 4 dígitos.)')
        else:
            # Verificar se a agência já existe
            if agencia_existe(bancos, agencia_numero):
                print(f'A agência {agencia_numero} já está registrada em outro banco.')
            else:
                nova_agencia = Agencia(agencia_numero)
                banco_encontrado['agencias'].append({"numero": nova_agencia.numero})
                salvar_dadosagencia(bancos)
                print('Agência cadastrada com sucesso!')
                return


# LISTAR AGÊNCIAS CADASTRADAS
def listar_agencias(bancos):
    if not bancos:
        print('Nenhum Banco Cadastrado.')
    else:
        for banco in bancos:
            agencias = ", ".join(agencia['numero'] for agencia in banco['agencias'])
            print(f'Banco: {banco["nome"]}, Agências: {agencias}')
    sleep(2)


# PESQUISAR UMA AGÊNCIA JÁ REGISTRADA
def pesquisar_agencia(bancos):
    agencia_numero = input('Digite o número da agência para pesquisar: ')
    for banco in bancos:
        for agencia in banco['agencias']:
            if agencia['numero'] == agencia_numero:
                print(f'Agência encontrada: {agencia_numero} no banco {banco["nome"]}')
                return
    print('Agência não encontrada.')
    sleep(2)


# EXCLUIR UMA AGÊNCIA
def excluir_agencia(bancos):
    agencia_numero = input('Digite o número da agência a ser excluída: ')
    for banco in bancos:
        for agencia in banco['agencias']:
            if agencia['numero'] == agencia_numero:
                banco['agencias'].remove(agencia)
                salvar_dadosagencia(bancos)
                print(f'Agência {agencia_numero} excluída com sucesso!')
                return
    print('Agência não encontrada.')
    sleep(2)


# Menu de Gerenciamento de Agências
def menu_agencias():
    bancos = carregar_dadosagencia()
    while True:
        cabecalho('GERENCIAR AGÊNCIAS'.center(50))
        resposta = menu(
            ['Nova Agência', 'Listar Agências', 'Pesquisar Agência', 'Excluir Agência', 'Voltar ao Menu Anterior'])
        if resposta == 1:
            cadastrar_agencia(bancos)
        elif resposta == 2:
            listar_agencias(bancos)
        elif resposta == 3:
            pesquisar_agencia(bancos)
        elif resposta == 4:
            excluir_agencia(bancos)
        elif resposta == 5:
            break
        else:
            print('ERRO - Digite uma opção válida!')
            sleep(2)