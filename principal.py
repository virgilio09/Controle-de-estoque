from cliente import Cliente
from pessoa import Pessoa
from estoque import Estoque
from produto import Produto
from funcionario import Funcionario
from loja import Loja


estoque = Estoque()



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

opcao = int(input("Escolha uma opcão: "))