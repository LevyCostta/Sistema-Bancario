# Sistema-Bancario

# Simulação de Sistema Bancário usando Programação Orientada a Objetos em Python

Nesta simulação nós teremos a criação de classes Python, construtores, encapsulamento de dados, agregação e composição, métodos com retorno e sem retorno, variáveis estáticas, variáveis públicas e privadas, e relacionamento entre objetos (um para um, um para muitos, muitos para um) usando List. Sim, o projeto faz uso extensivo de List, o que o torna muito rico para o aprendizado e fixação dos conhecimentos da linguagem Python e suas classes principais.



## O Diagrama de Classes Python
Antes de falarmos mais sobre o projeto, dê uma boa olhada no seu diagrama de classes:

![Diagrama de classe](https://acesseonline-arquivos-publicos.s3.us-east-2.amazonaws.com/exercicio_python/sistema_bancario_python_console_diagrama_classes.jpg)

## Como a aplicação está estruturada?

Como podemos ver no diagrama de classes, nós temos uma classe Sistema que contém zero ou vários objetos da classe Banco (relacionamento um para muitos). A classe Banco, por sua vez, possui uma List de objetos da classe Agência, ou seja, mais um relacionamento um para muitos, já que cada agência pertence a um único banco.

Cada agência pode possuir zero ou mais contas, e cada conta possui um List de objetos da classe Transação, o que nos permite registrar todas as operações nas contas e emitir o extrato bancário, com os débitos, créditos e transferências entre contas.

Tudo isso é feito por meio de vários menus de opções, como podemos ver na imagem a seguir:

![Menu](https://acesseonline-arquivos-publicos.s3.us-east-2.amazonaws.com/exercicio_python/sistema_bancario_python_console_menus.jpg)

## O fechamento com chave de ouro

O produto final da aplicação Python deverá ser um extrato bancário mostrando os dados da conta escolhida, o histórico de transações com data, tipo da transação e valor, e o saldo atual da conta, com ou sem limite. Veja na imagem abaixo a formatação apresentada (mesmo em modo texto):

![Extrato](https://acesseonline-arquivos-publicos.s3.us-east-2.amazonaws.com/exercicio_python/sistema_bancario_python_console_extrato.jpg)


## Checklist

- [ ]  Readme.md para documentar
- [ ]  Módulo e classe sistema
- [ ]  Módulo e classe banco
- [ ]  Módulo e classe agência
- [ ]  Módulo e classe pessoa
- [ ]  Módulo e classe conta
- [ ]  Módulo e classe transação
