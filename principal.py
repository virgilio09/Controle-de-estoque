from cliente import Cliente
from pessoa import Pessoa
from estoque import Estoque
from produto import Produto
from funcionario import Funcionario
from loja import Loja
import menus


estoque = Estoque()
loja = Loja()


while True:
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

    if(opcao == '1'):
        cliente = loja.buscar_cliente()
        if(cliente != []):
            menus.menu_cliente()
        else:
            print("\nCpf Invalido!\nContate seu vendedor!\n")

    elif(opcao == '2'):
        func = loja.buscar_funcionario()
        if(func != []):
            while True:
                opcao2 = menus.menu_func()
                if(opcao2 == '1'):
                    while True:
                        cadastros = menus.menu_cadastro()
                        if(cadastros == '1'):
                            estoque.cadastrar_produto()
                        elif(cadastros == '2'):
                            loja.cadastra_cliente()
                        elif(cadastros == '3'):
                            loja.cadastra_func()
                        elif(cadastros == '0'):
                            break
                elif(opcao2 == '2'):
                    while True:
                        remover = menus.menu_remover()
                        if(remover == '1'):
                            estoque.remover_produto()
                        elif(remover == '2'):
                            pass
                        elif(remover == '3'):
                            pass
                        elif(remover == '0'):
                            break
                elif(opcao2 == '3'):
                    pass
                elif(opcao2 == '0'):
                    break
        else:
            
            loja.cadastra_func() 
            
    elif(opcao == '0'):
        break

