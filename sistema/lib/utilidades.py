def linha():
    print('-'*50)

def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('ERRO - Por favor, digite um número inteiro valido.')
            continue
        except(KeyboardInterrupt):
            print('Usuario Preferiu não digitar esse número.')
            return 0
        else:
            return n

def cabecalho(txt):
    linha()
    print(txt.center(50))
    linha()

def menu(lista):
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    linha()
    opc = leiaint('Digite a Opção Desejada: ')
    return opc



