from controls import *

def main():
    #contantes imutaveis do sistema
    AGENCIA = "0001"
    LIMITE_DE_SAQUE = 3
    
    #saldo inicial da conta
    saldo = 0

    #limite monetário de saque 
    limite = 500

    #extrado inical da conta
    extrato = ""

    #numero de operações de saque
    n_op_saque = 0

    #limite de movimentações diárias
    limite_saque = 3

    #listas de usuarios e contas
    usuarios = []
    contas =[]

    #inicialização do sistema + mensagem de boas vindas + autor kkkkkkk
    prompt_init = """
    ###################################################################

    Bem-Vindo ao Sistema Bancário v2.0 ~~ By Gustavo Santos ~~ Python

    ###################################################################
    
    Digite \"I\" para Inicializar ==> """
    
    init = input(prompt_init).upper()

    while init =="I":
        #menu inicial + input user
        operacoes = menu_inicial()

        #operação que cria usuario
        if operacoes == "NU":
            new_user(usuarios)

        #operação para criação de nova conta para o usuario
        elif operacoes == "NC":
            #leitura de contas e referenciação de possivel conta
            n_conta = len(contas) + 1
            conta = new_conta(AGENCIA, n_conta, usuarios)

            # se conta não exixtir add conta
            if conta:
                contas.append(conta)

        #operação para listar contas cadastradas pelo usuario
        elif operacoes == "LCC":
            lista = len(contas)

            if  lista == 0:
                msg = """\n
                    ###################################################################

                                    Nenhuma conta cadastrada no momento! 
            
                    ###################################################################\n"""
                print(msg)
            
            else:
                list_conta(contas)

        #operação para realizar depósito
        elif operacoes == "D":
            #input para identificar valor digitado pelo usuario + efetuação do deposito
            valor = float(input("\tDigite o valor à ser depositado: "))
            
            saldo, extrato = deposito(saldo, valor, extrato)

        #operação para efetuar saque
        elif operacoes == "S":
            #input do user para captação de daos
            valor = float(input("\tDigite o valor que seja sacado: "))
            #parametros a serem passados para função
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                n_op_saque=n_op_saque,
                limite_saques=LIMITE_DE_SAQUE,
            )
        
        #operação para exibir extrato
        elif operacoes == "E":
            view_extrato(saldo, extrato=extrato)

        #operação "Sair/Encerrar" o sistema
        elif operacoes == "SE":
            break
        
        #codigopara evitar erros de digitação
        else:
            debug_error()

    #codigo para evitar erros na execução da inicializaçõa do codigo
    else:
        debug_error()
        return main()
    

main()