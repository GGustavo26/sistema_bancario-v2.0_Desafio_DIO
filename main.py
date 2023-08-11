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

    #inicialização do sistema + mesnagem de boas vindas + autor kkkkkkk
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
            print("novo usuario função")

        #operação para criação de nova conta para o usuario
        elif operacoes == "NC":
            print("nova conta função")

        #operação para listar contas cadastradas pelo usuario
        elif operacoes == "LCC":
            print("Listar contas cadastradas função")

        #operação para realizar depósito
        elif operacoes == "D":
            print("Depositar função")

        #operação para efetuar saque
        elif operacoes == "S":
            print("sacar função")
        
        #operação para exibir extrato
        elif operacoes == "E":
            print("extrato função")

        #operação "Sair/Encerrar" o sistema
        elif operacoes == "SE":
            break
        
        #codigopara evitar erros de digitação
        else:
            fal = """\n
            ###################################################################

                        Comando não encontrado! Tente Novamente. 
            
            ###################################################################\n"""
            print(fal)

    #codigo para evitar erros na execução da inicializaçõa do codigo
    else:
        error = """\n
        ###################################################################

                    Comando não encontrado! Tente Novamente. 
        
        ###################################################################\n"""
        print(error)
        return main()
    

main()