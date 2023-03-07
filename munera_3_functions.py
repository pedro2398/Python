from time import sleep


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
        ("Id não encontrado!")
        
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