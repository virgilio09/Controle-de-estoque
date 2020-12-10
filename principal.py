from cliente import Cliente
from pessoa import Pessoa
from estoque import Estoque
from produto import Produto
from funcionario import Funcionario
from loja import Loja
import menus


estoque = Estoque()
loja = Loja()
cliente = Cliente()


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

    if(opcao == '1'):#menuCliente
        cliente = loja.buscar_cliente()
        if(cliente != []):
            while True:
                opcao1 = menus.menu_cliente()
                if(opcao1 == '1'):
                    while True:
                        compra = menus.menu_compras()
                        if(compra == '1'):
                            loja.cliente.add_produto(loja.estoque)
                        elif(compra == '2'):
                            loja.cliente.rm_produto(loja.estoque)
                        elif(compra == '0'):
                            break
                elif(opcao1 == '2'):
                    pass
                elif(opcao1 == '0'):
                    break
        else:
            print("\nCpf Invalido!\nContate seu vendedor!\n")

    elif(opcao == '2'):#menuFunc
        func = loja.buscar_funcionario()
        if(func != []):
            while True:
                opcao2 = menus.menu_func()
                if(opcao2 == '1'):#cadastros
                    while True:
                        cadastros = menus.menu_cadastro()
                        if(cadastros == '1'):
                            loja.estoque.cadastrar_produto()
                        elif(cadastros == '2'):
                            loja.cadastra_cliente()
                        elif(cadastros == '3'):
                            loja.cadastra_func()
                        elif(cadastros == '0'):
                            break
                elif(opcao2 == '2'):#remover
                    while True:
                        remover = menus.menu_remover()
                        if(remover == '1'):
                            loja.estoque.remover_produto()
                        elif(remover == '2'):
                            loja.remove_cliente()
                        elif(remover == '3'):
                            loja.remove_func()
                        elif(remover == '0'):
                            break
                elif(opcao2 == '3'):#Analise
                    result = loja.buscar_cliente()
                    if(result != []):
                        loja.analise_compras(result[0])
                    else:
                        print("Nenhum cliente cadastrado!")
                elif(opcao2 == '4'):#Listar
                    while True:
                        lista = menus.menu_listar()
                        if(lista == '1'):#listarEstoque
                            loja.estoque.mostrar_produtos()
                        elif(lista == '2'):#listarFuncionarios
                            loja.mostrar_func()
                        elif(lista == '3'):#listarClientes
                            loja.mostrar_clientes()
                        elif(lista == '0'):#voltar
                            break
                elif(opcao2 == '0'):
                    break
        else:
            
            loja.cadastra_func() 
            
    elif(opcao == '0'):
        break

