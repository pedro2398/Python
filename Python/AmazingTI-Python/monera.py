from time import sleep
prin_opc = ""

emails = []
senhas =  []
nomes = []

cnpj = []
nomes_empresa = []
info_empresa = []
curtidas = []

opc = ""

while(prin_opc != 3):
    prin_opc = int(input(f"{'-=' * 5} Seja bem vindo(a) à Munera! {'=-' * 5}\n" +
                          "1 - Fazer Login/Cadastro\n" +
                          "2 - Ver empresas\n" +
                          "3 - Sair\n" + 
                          "Oque voçê deseja fazer: "
    ))

    print()
    print("Aguarde", end='')
    sleep(0.5)
    print(".", end='')
    sleep(0.5)
    print(".", end='')
    sleep(0.5)
    print(".")
    sleep(0.5)


    if(prin_opc == 1):

        opc = ""

        while(opc != 5):

            print()
            opc = int(input(
            "1 - Cadastrar usuario\n" +
            "2 - Cadastrar empresa\n" + 
            "3 - Fazer login usuario\n" + 
            "4 - Fazer login empresa\n" +
            "5 - Voltar\n" +
            "Escolha uma opção : "
            ))
            print()

            if(opc == 1):

                nomes.append(input("Informe o seu nome : "))
                emails.append(input("Informe o seu email: "))
                senhas.append(input("Informe a sua senha: "))
                print("Cadastro realizado com sucesso!")

            elif(opc == 2):

                cnpj.append(input("Informe o cnpj da empresa: "))
                nomes_empresa.append(input("Informe o nome da empresa : "))
                info_empresa.append(input("Use esse espaço para falar mais sobre a sua empresa : "))
                print("Cadastro realizado com sucesso!")
                curtidas.append(0)

            elif(opc == 3):

                res_e = False
                res_s = False
                pos = ""

                email_inserido = input("Informe o seu email : ")

                while(res_e == False):
                    for i in range(0, len(emails), 1):
                        if(emails[i] == email_inserido):
                            res_e = True
                            pos = i
                    if(res_e == False):
                        print("Email não encontrado!")
                        email_inserido = input("Informe o seu email : ")

                senha_inserida = input("Informe a sua senha : ")

                while(res_s == False):
                    if(senha_inserida == senhas[pos]):
                        print()

                        print(f"Seja bem-vindo {nomes[pos]}!")

                        print(f"\n{'=-' * 7} EMPRESAS {'-=' * 7}")

                        for j in range(0, len(nomes_empresa), 1):
                            print(f"{j + 1} - {nomes_empresa[j]}")
                            print("Sobre a empresa: ")
                            print(info_empresa[j])
                            print(f"CURTIDAS: {curtidas[j]}")
                            print()

                        index = ""
                        resp_c = input("Você deseja curtir alguma empresa? [S/N] : ").upper()

                        while(resp_c != 'S'):
                            if(resp_c == 'N'):
                                break
                            else:
                                print("Escolha uma opção válida!")
                                resp_c = input("Você deseja curtir alguma empresa? [S/N] : ").upper()

                        while(resp_c == 'S'): 
                            index = int(input("Qual o numero da empresa que voçê deseja curtir? : ")) - 1
                            curtidas[index] = curtidas[index] + 1

                            print(f"\n{'=-' * 7} EMPRESAS {'-=' * 7}")
                            for j in range(0, len(nomes_empresa), 1):
                                print()
                                print(f"{j + 1} - {nomes_empresa[j]}")
                                print("Sobre a empresa: ")
                                print(info_empresa[j])
                                print(f"CURTIDAS: {curtidas[j]}")
                                print()

                            resp_c = input("Você deseja curtir mais alguma empresa? [S/N] : ").upper()
                            while(resp_c != 'S'):
                                if(resp_c == 'N'):
                                    break
                                else:
                                    print("Escolha uma opção válida!")
                                    resp_c = input("Você deseja curtir mais alguma empresa? [S/N] : ").upper()

                        res_s = True

                    else:
                        print("Senha incorreta!")
                        senha_inserida = input("Informe a sua senha : ")

            elif(opc == 4):
                res_e = False
                res_s = False
                pos = ""

                email_inserido = input("Informe o seu email : ")

                while(res_e == False):
                    for i in range(0, len(emails), 1):
                        if(emails[i] == email_inserido):
                            res_e = True
                            pos = i
                    if(res_e == False):
                        print("Email não encontrado!")
                        email_inserido = input("Informe o email da empresa : ")

                senha_inserida = input("Informe a senha da empresa : ")

                while(res_s == False):
                    if(senha_inserida == senhas[pos]):
                        print(f"Seja bem-vindo {nomes_empresa[pos]}")
                        res_s = True
                    else:
                        print("Senha incorreta!")
                        senha_inserida = input("Informe a senha da empresa : ")

            elif(opc <= 0 or opc > 5):
                    print("Escolha uma opção válida!")
    elif(prin_opc == 2):
        c = 1
        
        print(f"\n{'=-' * 7} EMPRESAS {'-=' * 7}")
        for j in range(0, len(nomes_empresa), 1):
            print(f"{c} - {nomes_empresa[j]}")
            print("Sobre a empresa: ")
            print(info_empresa[j])
            print(f"CURTIDAS: {curtidas[j]}")
            print()
            c =+ 1
        print()

print("Programa encerrado!")
