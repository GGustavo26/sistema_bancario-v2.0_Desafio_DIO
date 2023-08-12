import time

#menu inicial geral e estilização geral do sistema
def menu_inicial():
    menu = """\n
    #####################\tMenu Inicial\t#######################

    [NU] Novo Usuário 
    [NC] Nova Conta
    [LCC] Listar contas Cadastradas

    ###################################################################

    [D] Depositar
    [S] Sacar
    [E] Extrato

    ###################################################################

    [SE] Sair\\Encerrar

    ###################################################################

    ==> """
    return input(menu).upper()

def debug_error():
    fal = """\n
        ###################################################################

                    Comando não encontrado! Tente Novamente. 
            
        ###################################################################\n"""
    return print(fal)

def new_user(usuarios):
    #input para criar conta e filtar se há algum dado igual já cadastrado
    cpf = input("\tDigite seu CPF (Apenas Números): ")
    usuario = userFilter(cpf, usuarios)

    if usuario:
        fal = """\n
        ###################################################################

            O CPF inserido já pertence a um usuário! Tente novamente!
            
        ###################################################################\n"""

        return print(fal)
    
    #tela de espera para inicir cadastro
    tempo = """\n
        ###################################################################

            Após alguns segundos iniciaremos o cadastro. Prepare-se!
            
        ###################################################################\n"""
    time.sleep(5)
    print(tempo)
    time.sleep(10)

    #input para cadastro completo xcaso o cpf não seja repetido
    nome = input("\tDigite seu Nome completo: ")
    d_nascimento = input("\tDigite sua data de Nascimento (dd-mm-aaa): ")
    endereco = input("\tDigite seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    #adição dos dados na lista 
    usuarios.append({"nome": nome, "data_nascimento": d_nascimento, "cpf": cpf, "endereco": endereco})

    #mensagem de boas vindas
    bv_nome = nome.split()[0]
    welcome = f"""\n
        ###################################################################

                    Usuário cadastrado com sucesso!
                    
                             Bem-vindo {bv_nome}!
            
        ###################################################################\n"""
    time.sleep(10)
    print(welcome)
    time.sleep(10)

def userFilter(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def new_conta(agencia, n_conta, usuarios):
    #idendificando o usuario para criação de conta
    cpf = input("\tDigite o CPF do usuário (Apenas Números): ")
    usuario = userFilter(cpf, usuarios)

    if usuario:
        cert = """\n
        ###################################################################

                            Conta cadastrada com sucesso!
            
        ###################################################################\n"""
        print(cert)
        return {"agencia": agencia, "n_conta": n_conta, "usuario": usuario}
    
    else:
        fal = """\n
        ###################################################################

                        Conta de Usuário não encontrada! 

            Por favor vefifique suas insformações e tente novamente! 
            
        ###################################################################\n"""
    return print(fal)
      
def list_conta(contas):
    for conta in contas:
        txt = f"""\n
        ###################################################################


                    Agência: {conta['agencia']}
                    Número da conta: {conta['n_conta']}
                    Titular da conta: {conta['usuario']['nome']}
                    
            
        ###################################################################\n"""
        print(txt)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Déposito realizado: R${valor:.2f}\n"
        
        msg_sucess = f"""\n
        ###################################################################

            Depósito no valor de R$ {valor:.2f}, realizado com sucesso!
            
        ###################################################################\n"""
        print(msg_sucess)
    else:
        falha = """\n
        ###################################################################

                Operação não realizada! O valor informado é inválido. 
                
                                 Tente Novamente. 
            
        ###################################################################\n"""
        print(falha)

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, n_op_saque, limite_saque):
    
    exce_limite = valor > limite
    exce_saldo = valor > saldo
    exce_saque = n_op_saque >= limite_saque

    if exce_limite:
        msg = """\n
        ###################################################################

        Operação não realizada! O valor informado excede o limite de saque. 
                
                                 Tente Novamente. 
            
        ###################################################################\n"""
        print(msg)
    
    elif exce_saldo:
        msg_2 = """\n
        ###################################################################

            Operação não realizada! Você não possui saldo suficiente. 
                
                                 Tente Novamente. 
            
        ###################################################################\n"""
        print(msg_2)

    elif exce_saque:
        msg_3 = """\n
        ###################################################################

          Operação não realizada! Você atingiu o número máximo de saques. 
                
                                 Tente Novamente. 
            
        ###################################################################\n"""
        print(msg_3) 

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque realizado: R$ {valor:.2f}\n"
        n_op_saque += 1
        msg_sucess = f"""\n
        ###################################################################

            Saque no valor de R$ {valor:.2f}, realizado com sucesso!
            
        ###################################################################\n"""
        print(msg_sucess)

    else:
        falha = """\n
        ###################################################################

                Operação não realizada! O valor informado é inválido. 
                
                                 Tente Novamente. 
            
        ###################################################################\n"""
        print(falha)

    return saldo, extrato

def view_extrato(saldo, /, *, extrato):
    variavel = "Não foram realizadas operações." if not extrato else extrato
    
    text = f"""\n
        ###################################################################
                              
                              ~~    Extrato    ~~
                
                
                {variavel} 
                

                Saldo: R$ {saldo:.2f}
        ###################################################################\n"""
    print(text)

