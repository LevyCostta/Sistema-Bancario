from time import sleep
import json
import os
from utilidades import *

# Nome do arquivo onde os dados serão salvos
ARQUIVO_PESSOAS = 'pessoas.json'

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

# Função para carregar os dados do arquivo JSON
def carregar_dadospessoa():
    if os.path.exists(ARQUIVO_PESSOAS):
        with open(ARQUIVO_PESSOAS, 'r') as arquivo:
            dados = json.load(arquivo)
            return [Pessoa(p['nome'], p['idade'], p['cpf']) for p in dados]
    return []

def titular_existe(pessoas, nome=None, cpf=None):
    """Verifica se o titular existe no arquivo JSON."""
    if os.path.exists(ARQUIVO_PESSOAS):
        with open(ARQUIVO_PESSOAS, 'r') as arquivo:
            pessoas = json.load(arquivo)
            for pessoa in pessoas:
                if pessoa['nome'] == nome or pessoa['cpf'] == cpf:
                    return True
    return False

# Função para salvar os dados no arquivo JSON
def salvar_dadospessoas(pessoas):
    with open(ARQUIVO_PESSOAS, 'w') as arquivo:
        json.dump([{'nome': p.nome, 'idade': p.idade, 'cpf': p.cpf} for p in pessoas], arquivo, indent=4)

# Função para verificar se já existe uma pessoa cadastrada com o nome digitado
def pessoa_existe(pessoas, nome=None, cpf=None):
    for pessoa in pessoas:
        if (nome and pessoa.nome == nome) or (cpf and pessoa.cpf == cpf):
            return True
    return False

# CADASTRO DE PESSOAS
def cadastrar_pessoa(pessoas):
    while True:
        nome = input('Digite seu nome: ').title()
        if pessoa_existe(pessoas, nome=nome):
            print(f'Já existe uma pessoa cadastrada com o nome {nome}!')
            return
        elif nome == "":
            print('\n***Nome não pode ser vazio***')
        elif len(nome) < 3:
            print('Nome muito curto, digite um nome com pelo menos 3 caracteres\n')
        else:
            break

    # IDADE
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            if idade <= 0:
                print("\n***Idade inválida, digite uma idade válida***\n")
            else:
                break
        except ValueError:
            print("\n***Idade inválida, digite uma idade válida***\n")

    # CPF
    while True:
        cpf = input("Digite seu CPF (apenas números, exatamente 11 dígitos): ")
    
        if cpf == "":
            print("\n***CPF não pode ser vazio***")
        elif not cpf.isdigit() or len(cpf) != 11:
            print("\n***CPF inválido, digite um CPF válido (apenas números, exatamente 11 dígitos)***\n")
        elif pessoa_existe(pessoas, cpf=cpf):
            print(f'Já existe uma pessoa cadastrada com o CPF {cpf}!')
        else:
            break

    pessoa = Pessoa(nome, idade, cpf)
    pessoas.append(pessoa)
    salvar_dadospessoas(pessoas)
    print('Pessoa Cadastrada com Sucesso!')

# LISTAR PESSOAS
def listar_pessoas(pessoas):
    if not pessoas:
        print('Nenhuma Pessoa Cadastrada.')
    else:
        for pessoa in pessoas:
            print(f'Nome: {pessoa.nome}, Idade: {pessoa.idade}, CPF: {pessoa.cpf}')

# PESQUISAR PESSOA
def pesquisar_pessoa(pessoas):
    nome = input('Digite o nome da pessoa que deseja pesquisar: ').title()
    for pessoa in pessoas:
        if pessoa.nome == nome:
            print('PESSOA ENCONTRADA, AGUARDE...')
            print('')
            print('-' * 50)
            sleep(2)
            print(f'Nome: {pessoa.nome}, Idade: {pessoa.idade}, CPF: {pessoa.cpf}')
            sleep(3)
            return
    print('Pessoa não encontrada.')

# EXCLUIR PESSOA
def excluir_pessoa(pessoas):
    nome = input('Digite o nome da pessoa que deseja excluir: ').title()
    for pessoa in pessoas:
        if pessoa.nome == nome:
            pessoas.remove(pessoa)
            salvar_dadospessoas(pessoas)
            print('Pessoa Excluída com sucesso!')
            return
    print('Pessoa não encontrada.')

# ATUALIZAR PESSOA
def atualizar_pessoa(pessoas):
    nome = input('Digite o nome da pessoa que deseja atualizar: ').title()
    for pessoa in pessoas:
        if pessoa.nome == nome:
            # ATUALIZAR O NOME
            while True:
                novo_nome = input('Digite o novo nome: ').title()
                if pessoa_existe(pessoas, nome=novo_nome):
                    print(f'\n*** Já existe uma pessoa cadastrada com o nome {novo_nome} ***\n')
                elif novo_nome == "":
                    print('\nNome não pode ser vazio, digite novamente.\n')
                elif len(novo_nome) < 3:
                    print('\nNome muito curto, digite um nome com pelo menos 3 caracteres.\n')
                else:
                    pessoa.nome = novo_nome
                    break

            # ATUALIZAR IDADE
            while True:
                try:
                    nova_idade = int(input('Digite a nova idade: '))
                    if nova_idade <= 0:
                        print('\n*** IDADE INVÁLIDA...Digite uma idade válida ***\n')
                    else:
                        pessoa.idade = nova_idade  # Corrigido para atribuição
                        break
                except ValueError:
                    print('\n*** IDADE INVÁLIDA...Digite uma idade válida ***\n')

            # ATUALIZAR CPF
            while True:
                novo_cpf = input('Digite o novo CPF (apenas números, exatamente 11 dígitos): ')
                if not novo_cpf.isdigit() or len(novo_cpf) != 11:
                    print('\n***CPF inválido, digite um CPF válido (apenas números, exatamente 11 dígitos)***\n')
                elif pessoa_existe(pessoas, cpf=novo_cpf):
                    print(f'Já existe uma pessoa cadastrada com o CPF {novo_cpf}!')
                elif novo_cpf == "":
                    print('** CPF não pode ser vazio. ***')
                else:
                    pessoa.cpf = novo_cpf
                    break
            salvar_dadospessoas(pessoas)
            print('Pessoa Atualizada Com Sucesso!')
            return
    print('Pessoa não Encontrada.')

# MENU DE GERENCIAMENTO DE PESSOAS
def menu_pessoas():
    pessoas = carregar_dadospessoa()  # Corrigido para chamar a função
    while True:
        cabecalho('GERENCIAR PESSOAS'.center(50))
        resposta = menu(['Nova Pessoa', 'Listar Pessoas', 'Pesquisar Pessoas', 'Excluir Pessoa', 'Atualizar Pessoa', 'Voltar ao Menu Anterior'])
        if resposta == 1:
            cadastrar_pessoa(pessoas)
        elif resposta == 2:
            listar_pessoas(pessoas)
        elif resposta == 3:
            pesquisar_pessoa(pessoas)
        elif resposta == 4:
            excluir_pessoa(pessoas)
        elif resposta == 5:
            atualizar_pessoa(pessoas)
        elif resposta == 6:
            break
        else:
            print('ERRO - Digite uma opção válida!')
        sleep(2)