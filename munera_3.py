from time import sleep
import random
import munera_3_functions

login = "munera@" # login para iniciar o programa
senha = "1234"    # senha para iniciar o programa


resp_login = ''
resp_senha = ''

acessos_cadastrados = []
cadastros_PF = []
cadastros_PJ = []
calendario = []

while resp_login != login or resp_senha != senha :
    print(f"{'-=' * 5} Login ADM! {'=-' * 5}")
    resp_login = str(input("Informe o seu login: "))
    resp_senha = str(input("Informe a sua senha: "))
    print()

    munera_3_functions.processandoDef()

    if resp_login != login or resp_senha != senha:
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

while opcao_adm != 5:
    opcao_adm = int(input(
                          '1 - Controle de acessos \n' +
                          '2 - Alteração de cadastros \n' +
                          '3 - Configuração da agenda \n' +
                          '4 - Acesso ao banco de dados\n' + 
                          '5 - Encerrar programa \n' +
                          'Escolha uma opção: ' )) 
    print()
    
    munera_3_functions.processandoDef()
    
    while opcao_adm == 1:
        opcao_adm_1 = 0
        print(f"{'-=' * 5} Controle de acesso {'=-' * 5}")
        opcao_adm_1 = int(input("1 - Cadastro de acessos \n" + 
                                "2 - Edição dos acessos \n" +
                                "3 - Exclusão de acessos\n"))

        munera_3_functions.processandoDef()

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

            munera_3_functions.acaoDef("Cadastrando", "Cadastro concluido!")

        elif opcao_adm_1 == 2:

            print()
            munera_3_functions.exibirAcessos(acessos_cadastrados)
            print()

            esc = int(input(  
                    "1 - Nome\n2 - Cargo\n3 - Tipo de acesso\n"
                    "Oque voçê deseja alterar? : "))


            id_edit = int(input("Qual o Id do acesso que voçê deseja alterar? : "))

            if esc == 1:
                nome_edit = str(input("Qual é o novo nome?: "))
                print()

                for cadastros in acessos_cadastrados:
                    if cadastros['id'] == id_edit:
                        cadastro['nome'] = nome_edit

            elif esc == 2:
                cargo_edit = str(input("Qual é o novo cargo ?: "))
                print()

                for cadastros in acessos_cadastrados:
                    if cadastros['id'] == id_edit:
                        cadastro['cargo'] = cargo_edit

            elif esc == 3:
                acesso_edit = str(input("Qual é o novo tipo de acesso?: "))
                print()

                for cadastros in acessos_cadastrados:
                    if cadastros['id'] == id_edit:
                        cadastro['tipo_acesso'] = acesso_edit

            else:
                print("Opção inválida!")

            munera_3_functions.acaoDef("Alterando", "Alteração concluida!")


        elif opcao_adm_1 == 3:
            munera_3_functions.exibirAcessos(acessos_cadastrados)
            print()

            id_exc = int(input("Digite o id de qual cadastro deseja excluir: "))

            munera_3_functions.excluirAcessos(acessos_cadastrados, id_exc)
        
        else:
            print("Opção inválida!")

        break

    while opcao_adm == 2:

        print(f"{'-=' * 5} Alteração de cadastros {'=-' * 5}")
        opcao_adm_2 = int(input("1 - Cadastro de PF \n" + 
                                "2 - Cadastro de PJ\n"+
                                 "Escolha uma opção: "
                                ))
        print()

        if opcao_adm_2 == 1:
             opcao_adm_2_PF = int(input(f"1 - Adicionar\n" +
                                         "2 - Editar\n" +
                                         "3 - Excluir\n" +
                                         "Escolha uma opção: "
             ))
             
             if opcao_adm_2_PF == 1:

                munera_3_functions.processandoDef()

                cpf = str(input("Informe o CPF: "))
                nome_PF = str(input("Informe o nome: "))
                data_Nasc_PF = str(input("Informe a data de nascimento: "))
                endereco_PF = str(input("Infome o endereço: "))
                telefone_PF = str(input("Informe o telefone: "))
                email_PF = str(input("Informe o email: "))

                cadastro_PF = {"cpf": cpf, "nome": nome_PF, "dataNasc": data_Nasc_PF, "endereco": endereco_PF, "telefone": telefone_PF, "email": email_PF}
                cadastros_PF.append(cadastro_PF)

                munera_3_functions.acaoDef("Cadastrando", "Cadstro concluido!")

             elif opcao_adm_2_PF == 2:
        
                esc = int(input(  
                        "\n1 - nome\n2 - data de nascimento\n3 - Telefone\n4 - Endereço\n5 - Email\n"
                        "Oque voçê deseja alterar? : "))

                print()
                munera_3_functions.exibirAcessos(cadastros_PF)
                print()

                cpf_edit = str(input("Qual o cpf do acesso que voçê deseja alterar? : "))

                if esc == 1:
                    nome_edit = str(input("Qual é o novo nome?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastros['nome'] = nome_edit

                elif esc == 2:
                    data_edit = str(input("Qual a nova data?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastros['dataNasc'] = data_edit

                elif esc == 3:
                    endereco_edit = str(input("Qual é o novo endereço?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastros['endereco'] = endereco_edit
                
                elif esc == 4:
                    telefone_edit = str(input("Qual é o novo telefone?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastro['telefone'] = telefone_edit

                elif esc == 5:
                    email_edit = str(input("Qual é o novo email?: "))
                    print()

                    for cadastros in cadastros_PF:
                        if cadastros['cpf'] == cpf_edit:
                            cadastros['email'] = email_edit

                else:
                    print("Opção inválida!")

                munera_3_functions.acaoDef("Alterando", "Alteração concluida!")

             elif opcao_adm_2_PF == 3:

                munera_3_functions.processandoDef()

                munera_3_functions.exibirAcessos(cadastros_PF)
                print()

                cpf_exc = str(input("Informe o cpf para exclusão: "))

                munera_3_functions.excluirAcessos_PF(cadastros_PF, cpf_exc)
            
             else:
                 print("Opção inválida!")

        elif opcao_adm_2 == 2:
             opcao_adm_2_PJ = int(input(f"1 - Adicionar\n" +
                                         "2 - Editar\n" +
                                         "3 - Excluir\n" +
                                         "Escolha uma opção: "
             ))
             
             if opcao_adm_2_PJ == 1:

                munera_3_functions.processandoDef()

                cnpj = str(input("Informe o CNPJ: "))
                razaoSocial = str(input("Informe a razão social: "))
                endereco_Pj = str(input("Infome o endereço: "))
                telefone_Pj = str(input("Informe o telefone: "))
                email_Pj = str(input("Informe o email: "))

                cadastro_PJ = {"cnpj": cnpj, "razaoSocial": razaoSocial, "endereco": endereco_Pj, "telefone": telefone_Pj, "email": email_Pj}
                cadastros_PJ.append(cadastro_PJ)

                munera_3_functions.acaoDef("Cadastrando", "Cadstro concluido!")

             elif opcao_adm_2_PJ == 2:
        
                esc = int(input(  
                        "\n1 - Razão social\n2 - Endereço\n3 - Telefone\n4 - Email\n"
                        "Oque voçê deseja alterar? : "))

                print()
                munera_3_functions.exibirAcessos(cadastros_PJ)
                print()

                cnpj_edit = str(input("Qual o CNPJ do acesso que voçê deseja alterar? : "))

                if esc == 1:
                    rs_edit = str(input("Qual é a nova razão social?: "))
                    print()

                    for cadastros in cadastros_PJ:
                        if cadastros['cnpj'] == cnpj_edit:
                            cadastros['razaoSocial'] = rs_edit

                elif esc == 2:
                    endereco_edit = str(input("Qual é o novo endereço?: "))
                    print()

                    for cadastros in cadastros_PJ:
                        if cadastros['cnpj'] == cnpj_edit:
                            cadastros['endereco'] = endereco_edit
                
                elif esc == 3:
                    telefone_edit = str(input("Qual é o novo telefone?: "))
                    print()

                    for cadastros in cadastros_PJ:
                        if cadastros['cnpj'] == cnpj_edit:
                            cadastro['telefone'] = telefone_edit

                elif esc == 4:
                    email_edit = str(input("Qual é o novo email?: "))
                    print()

                    for cadastros in cadastros_PJ:
                        if cadastros['cnpj'] == cnpj_edit:
                            cadastros['email'] = email_edit

                else:
                    print("Opção inválida!")

                munera_3_functions.acaoDef("Alterando", "Alteração concluida!")

             elif opcao_adm_2_PJ == 3:

                munera_3_functions.processandoDef()

                munera_3_functions.exibirAcessos(cadastros_PJ)
                print()

                cnpj_exc = str(input("Informe o CNPJ para exclusão: "))

                munera_3_functions.excluirAcessos_PJ(cadastros_PJ, cnpj_exc)
        
             else:
                print("Opção inválida!")

        break

    while opcao_adm == 3:
        
        opcao_adm_3 = int(input(f"{'-=' * 5} Configuração do calendario {'-=' * 5}\n" + 
                                 "1 - Atualizar sincronização com o Google\n" +
                                 "2 - Incluir eventos\n" +
                                 "3 - Exibir eventos\n"+
                                 "Escolha uma opção : "
                                 ))
        
        munera_3_functions.processandoDef()

        if opcao_adm_3 == 1:
            munera_3_functions.acaoDef("Sincronizando", "Sincronização concluida com sucesso!")

        elif opcao_adm_3 == 2:
            tit_evento = str(input("Titulo: "))
            data_evento = str(input("Data: "))
            link_evento = str(input("Link: "))
            empresa_evento = str(input("Empresa: "))

            evento = {"titulo": tit_evento, "data": data_evento, "link": link_evento, "empresa": empresa_evento}
            calendario.append(evento)

            munera_3_functions.acaoDef("Adicionando evento", "Evento cadastrado!")
        
        elif opcao_adm_3 == 3:

            for evento in calendario:
                    print(f"Titulo: {evento['titulo']} || Data: {evento['data']} || Link: {evento['link']} || Empresa: {evento['empresa']}")
            print()
        
        else:
            print("Opção inválida!")

        break

    while opcao_adm == 4:

        opcao_adm_4 = int(input(f"{'-=' * 5} Acesso ao banco de dados {'-=' * 5}\n" + 
                                "1 - Cadastros de pessoas fisicas\n2 - Cadastros de empresas\nEscolha uma opção: "
                                ))
        
        munera_3_functions.processandoDef()

        if opcao_adm_4 == 1:
            for pf in cadastros_PF:
                print(f"CPF: {pf['cpf']} || Nome: {pf['nome']} || Data de nascimento: {pf['dataNasc']} || Endereco: {pf['endereco']} || Telefone: {pf['telefone']} || Email: {pf['email']}")

            print()
            
        elif opcao_adm_4 == 2:
            for pj in cadastros_PJ:
                print(f"CNPJ: {pj['cnpj']} || Razão social {pj['razaoSocial']} || Endereco: {pj['endereco']} || Telefone: {pj['telefone']} || Email: {pj['email']} ")    

            print()

        else:
            print("Opção inválida!")

        break