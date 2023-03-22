from time import sleep


def processandoDef():
    print("Processando", end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.')
    print()

def acaoDef(str1, str2):
    print(str1, end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.')
    print(str2)
    sleep(0.5)
    print()

def exibirAcessos(Array):

    if len(Array) == 0:
        print("Sem cadastros registrados!")
    else:
        for cadastros in Array:
            print(cadastros)

def excluirAcessos(Array, id):
    verify = False

    for cadastros in Array:
        if cadastros['id'] == id:
            Array.remove(cadastros)
            verify = True

    if verify == False:
        print("Procurando", end='')
        sleep(0.3)
        print('.', end='')
        sleep(0.3)
        print('.', end='')
        sleep(0.3)
        print('.')
        sleep(0.5)
        print()
        print("Id não encontrado!")
        print()
        
    else:
         print("Excluindo", end='')
         sleep(0.3)
         print('.', end='')
         sleep(0.3)
         print('.', end='')
         sleep(0.3)
         print('.')
         print("Excluido!")
         sleep(0.5)
         print()

def excluirAcessos_PF(Array, cpf):

    verify = False

    for cadastros in Array:
        if cadastros['cpf'] == cpf:
            Array.remove(cadastros)
            verify = True

    if verify == False:
        print("Procurando", end='')
        sleep(0.3)
        print('.', end='')
        sleep(0.3)
        print('.', end='')
        sleep(0.3)
        print('.')
        sleep(0.5)
        print()
        print("CPF não encontrado!")
        print()
        
    else:
         print("Excluindo", end='')
         sleep(0.3)
         print('.', end='')
         sleep(0.3)
         print('.', end='')
         sleep(0.3)
         print('.')
         print("Excluido!")
         sleep(0.5)
         print()

def excluirAcessos_PJ(Array, cnpj):

    verify = False

    for cadastros in Array:
        if cadastros['cnpj'] == cnpj:
            Array.remove(cadastros)
            verify = True

    if verify == False:
        print("Procurando", end='')
        sleep(0.3)
        print('.', end='')
        sleep(0.3)
        print('.', end='')
        sleep(0.3)
        print('.')
        sleep(0.5)
        print()
        print("CNPJ não encontrado!")
        print()
        
    else:
         print("Excluindo", end='')
         sleep(0.3)
         print('.', end='')
         sleep(0.3)
         print('.', end='')
         sleep(0.3)
         print('.')
         print("Excluido!")
         sleep(0.5)
         print()
