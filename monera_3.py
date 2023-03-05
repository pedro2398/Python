from time import sleep
import random

login = "munera@"
senha = "1234"

resp_login = ''
resp_senha = ''

acessos_cadastrados = []

while resp_login != login and resp_senha != senha :
    print(f"{'-=' * 5} Login ADM! {'=-' * 5}")
    resp_login = str(input("Informe o seu login: "))
    resp_senha = str(input("Informe a sua senha: "))
    print()

    print("Processando", end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.')

    if resp_login != login and resp_senha != senha:
        print()
        print('Senha ou login incorretos!')
        print()
        sleep(1.5)

sleep(1)
print()

print("Seja bem vindo ADM! ")
sleep(0.5)
print()

opcao_adm = 0

while opcao_adm != 7:
    opcao_adm = int(input('Oque deseja fazer? : \n' + 
                          '1 - Controle de acessos \n' +
                          '2 - Alteração de cadastros \n' +
                          '3 - Configuração da agenda \n' +
                          '4 - Configuração do curso \n' + 
                          '5 - Acesso ao banco de dados\n' + 
                          '6 - Outros assuntos \n' +
                          '7 - Encerrar programa' )) 
    print()
    sleep(1)
    
    while opcao_adm == 1:
        opcao_adm_1 = 0
        print(f"{'-=' * 5} Controle de acesso {'=-' * 5}")
        opcao_adm_1 = int(input("1 - Cadastro de acessos \n" + 
                                "2 - Edição dos acessos \n" +
                                "3 - Exclusão de acessos"))
        if(opcao_adm_1 == 1):
            
        #   id = random.radint(100, 200)
        #   verificador = True

        #   if acessos_cadastrados.
        #        while verifcador == True:
        #            for cadastros in acessos_cadastrados:
        #                if cadastro['id'] == id:
        #                    id = random.radint(100, 200)
        #   (Verificar se o Id ja exite para n criar repeticao)

                

            nome = str(input("Informe o seu nome: "))
            cargo  = str(input("Informe o seu cargo: "))
            tipo_acesso = str(str("Tipo de acesso: "))

            cadastro = {"id": id,"nome": nome, "cargo": cargo, "tipo_acesso": tipo_acesso}
    
            acessos_cadastrados.append()
