from ast import Break
from time import sleep
import random
from turtle import st
import munera_3_functions

login = "monera@"
senha = "1234"

resp_login = ''
resp_senha = ''

acessos_cadastrados = []
cadastros_PF = []

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
    opcao_adm = int(input(
                          '1 - Controle de acessos \n' +
                          '2 - Alteração de cadastros \n' +
                          '3 - Configuração da agenda \n' +
                          '4 - Acesso ao banco de dados\n' + 
                          '5 - Encerrar programa \n' +
                          'Escolha uma opção: ' )) 
    print()
    
    print("Processando", end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.')
    
    while opcao_adm == 1:
        opcao_adm_1 = 0
        print(f"{'-=' * 5} Controle de acesso {'=-' * 5}")
        opcao_adm_1 = int(input("1 - Cadastro de acessos \n" + 
                                "2 - Edição dos acessos \n" +
                                "3 - Exclusão de acessos\n"))

        print("Processando", end='')
        sleep(0.3)
        print('.', end='')
        sleep(0.3)
        print('.', end='')
        sleep(0.3)
        print('.')
        print()

        if opcao_adm_1 == 1:

            id = random.randint(100, 999)

            cont = 0

            while cont != len(acessos_cadastrados):
                for cadastros in acessos_cadastrados:
                    if cadastros['id'] == id:
                        id = random.randint(100, 999)
                    
                        cont = 0
                    else:
                        cont = cont + 1
                        print(cont)

            nome = str(input("Informe o nome: "))
            cargo  = str(input("Informe o cargo: "))
            tipo_acesso = str(input("Tipo de acesso: "))

            cadastro = {"id": id,"nome": nome, "cargo": cargo, "tipo_acesso": tipo_acesso}

            acessos_cadastrados.append(cadastro)

            print("Cadastrando", end='')
            sleep(0.3)
            print('.', end='')
            sleep(0.3)
            print('.', end='')
            sleep(0.3)
            print('.')
            print("Cadastro concluido!")
            sleep(0.5)
            print()

        if opcao_adm_1 == 2:

            esc = int(input(  
                    "1 - Nome\n2 - Cargo\n3 - Tipo de acesso\n"
                    "Oque voçê deseja alterar? : "))

            print()
            munera_3_functions.exibirAcessos(acessos_cadastrados)
            print()

            id_edit = int(input("Qual o Id do acesso que voçê deseja alterar? : "))

            if esc == 1:
                nome_edit = str(input("Qual é o novo nome?: "))
                print()

                for cadastros in acessos_cadastrados:
                    if cadastros['id'] == id_edit:
                        cadastro['nome'] = nome_edit

                print("Alterando", end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.')
                print("Atualização concluida!")
                sleep(0.5)
                print()

            if esc == 2:
                cargo_edit = str(input("Qual é o novo cargo ?: "))
                print()

                for cadastros in acessos_cadastrados:
                    if cadastros['id'] == id_edit:
                        cadastro['cargo'] = cargo_edit

                print("Alterando", end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.')
                print("Atualização concluida!")
                sleep(0.5)
                print()

            if esc == 3:
                acesso_edit = str(input("Qual é o novo tipo de acesso?: "))
                print()

                for cadastros in acessos_cadastrados:
                    if cadastros['id'] == id_edit:
                        cadastro['tipo_acesso'] = acesso_edit

                print("Alterando", end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.')
                print("Atualização concluida!")
                sleep(0.5)
                print()


        if opcao_adm_1 == 3:
            munera_3_functions.exibirAcessos(acessos_cadastrados)
            print()

            id_exc = int(input("Digite o id de qual cadastro deseja excluir: "))

            munera_3_functions.excluirAcessos(acessos_cadastrados, id_exc)
        
        break

    while opcao_adm == 2:

        print(f"{'-=' * 5} Alteração de cadastros {'=-' * 5}")
        opcao_adm_2 = int(input("1 - Cadastro de PF \n" + 
                                "2 - Cadastro de PJ "
                                ))
        print()

        if opcao_adm_2 == 1:
             opcao_adm_2_PF = int(input(f"1 - Adicionar\n" +
                                         "2 - Excluir\n" +
                                         "3 - Editar "
             ))
             
             if opcao_adm_2_PF == 1:

                print("Carregando", end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.')
                sleep(0.5)
                print()

                cpf = str(input("Informe o CPF: "))
                nome_PF = str(input("Informe o nome: "))
                data_Nasc_PF = str(input("Informe a data de nascimento: "))
                endereco_PF = str(input("Infome o endereço: "))
                telefone_PF = str(input("Informe o telefone: "))
                email_PF = str(input("Informe o email: "))

                cadastro_PF = {"cpf": cpf, "nome": nome_PF, "dataNasc": data_Nasc_PF, "endereco": endereco_PF, "telefone": telefone_PF, "email": email_PF}
                cadastros_PF.append(cadastro_PF)

                print("Cadastrando", end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.')
                print("Cadastro realizado!")
                sleep(0.5)
                print()

             elif opcao_adm_2_PF == 2:

                print("Carregando", end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.', end='')
                sleep(0.3)
                print('.')
                sleep(0.5)
                print()

                munera_3_functions.exibirAcessos(cadastros_PF)
                print()

                cpf_exc = str(input("Informe o cpf para exclusão: "))

                munera_3_functions.excluirAcessos_PF(cadastros_PF, cpf_exc)
        
             elif opcao_adm_2_PF == 3:

                esc = int(input(  
                        "\n1 - nome\n2 - data de nascimento\n3 - Telefone\n4 - Endereço\n5 - Email\n"
                        "Oque voçê deseja alterar? : "))

                print()
                munera_3_functions.exibirAcessos(cadastros_PF)
                print()

                cpf_edit = int(input("Qual o cpf do acesso que voçê deseja alterar? : "))

                if esc == 1:
                    nome_edit = str(input("Qual é o novo nome?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            print("Foi!")
                            cadastros['nome'] = nome_edit

                    print("Alterando", end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.')
                    print("Atualização concluida!")
                    sleep(0.5)
                    print()

                if esc == 2:
                    data_edit = str(input("Qual a nova data?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastros['dataNasc'] = data_edit

                    print("Alterando", end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.')
                    print("Atualização concluida!")
                    sleep(0.5)
                    print()

                if esc == 3:
                    endereco_edit = str(input("Qual é o novo endereço?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastros['endereco'] = endereco_edit

                    print("Alterando", end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.')
                    print("Atualização concluida!")
                    sleep(0.5)
                    print()
                
                if esc == 4:
                    telefone_edit = str(input("Qual é o novo telefone?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastro['telefone'] = telefone_edit

                    print("Alterando", end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.')
                    print("Atualização concluida!")
                    sleep(0.5)
                    print()

                if esc == 5:
                    email_edit = str(input("Qual é o novo email?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastros['email'] = email_edit

                    print("Alterando", end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.', end='')
                    sleep(0.3)
                    print('.')
                    print("Atualização concluida!")
                    sleep(0.5)
                    print()
        break