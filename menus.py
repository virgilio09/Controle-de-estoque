def menu_principal(nome):
    print("\nNome da loja {}".format(nome))
    print("-"*25)
    print("|     Menu Principal    |")
    print("-"*25)
    print("|                       |")
    print("| 1 - Cliente           |")
    print("|                       |")
    print("| 2 - Vendedor          |")
    print("|                       |")
    print("| 0 - Sair              |")
    print("-"*25)

    opcao = input("Escolha uma opcão: ")
    return opcao


def menu_cliente():
    print("-"*25)
    print("|     Menu Cliente      |")
    print("-"*25)
    print("|                       |")
    print("| 1 - Comprar/Retirar   |")
    print("|                       |")
    print("| 2 - Listar Produtos   |")
    print("|                       |")
    print("| 0 - Voltar            |")
    print("-"*25)

    opcao = input("Escolha uma opcão: ")
    return opcao

def menu_compras():
    print("-"*25)
    print("|     Menu Cliente      |")
    print("-"*25)
    print("|                       |")
    print("| 1 - Adicionar Produto |")
    print("|                       |")
    print("| 2 - Retirar Produto   |")
    print("|                       |")
    print("| 0 - Voltar            |")
    print("-"*25)

    opcao = input("Escolha uma opcão: ")
    return opcao

def menu_func():
    print("-"*25)
    print("|     Menu Funcionario  |")
    print("-"*25)
    print("|                       |")
    print("| 1 - Cadastros         |")
    print("|                       |")
    print("| 2 - Remover           |")
    print("|                       |")
    print("| 3 - Analise           |")
    print("|                       |")
    print("| 4 - Listar            |")
    print("|                       |")
    print("| 0 - Voltar            |")
    print("-"*25)

    opcao = input("Escolha uma opcão: ")
    return opcao

def menu_cadastro():
    print("-"*25)
    print("|     Menu Funcionario  |")
    print("-"*25)
    print("|                       |")
    print("| 1 - Cadastrar Produto |")
    print("|                       |")
    print("| 2 - Cadastrar Cliente |")
    print("|                       |")
    print("| 3 - Cadastrar Func.   |")
    print("|                       |")
    print("| 0 - Voltar            |")
    print("-"*25)

    opcao = input("Escolha uma opcão: ")
    return opcao

def menu_remover():
    print("-"*25)
    print("|     Menu Funcionario  |")
    print("-"*25)
    print("|                       |")
    print("| 1 - Remover Produto   |")
    print("|                       |")
    print("| 2 - Remover Cliente   |")
    print("|                       |")
    print("| 3 - Remover Func.     |")
    print("|                       |")
    print("| 0 - Voltar            |")
    print("-"*25)

    opcao = input("Escolha uma opcão: ")
    return opcao

def menu_listar():
    print("-"*25)
    print("|     Menu Funcionario  |")
    print("-"*25)
    print("|                       |")
    print("| 1 - Listar Estoque    |")
    print("|                       |")
    print("| 2 - Listar Func       |")
    print("|                       |")
    print("| 3 - Listar Clientes   |")
    print("|                       |")
    print("| 0 - Voltar            |")
    print("-"*25)

    opcao = input("Escolha uma opcão: ")
    return opcao
