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

