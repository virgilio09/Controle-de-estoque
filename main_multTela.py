import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QListWidgetItem

from interface.tela_cadastro_cliente import Tela_cadastro_cliente
from interface.tela_cadastro_funcionario import *
from interface.tela_cadastro_produto import Tela_cadastro_produto
from interface.tela_inicial import Tela_inicial
from interface.tela_primeiro_acesso import Tela_primeiro_acesso
from interface.tela_login import Tela_login_func, Tela_login_cli
from interface.tela_op_funcionario import Tela_op_funcionario
from interface.tela_tipo_cadastro import Tela_tipo_cadastro
from interface.tela_listagens import Tela_listagens
from interface.tela_tipo_exclusao import Tela_tipo_exclusao
from interface.tela_listDados import Tela_listDados
from interface.tela_vendas import Tela_vendas
from interface.tela_validar import Tela_validar
from interface.telaLista import TelaListProd, TelaListaCli, TelaListaFunc

from cadastra_produtos import *
from cadastra_pessoa import *
# from vendas import *

class Ui_main(QtWidgets.QWidget):

	'''
	class Ui_main()
	---------------
	Responsavel por conter o layout de todas as telas, estancia

	Funções
	-------
	setupUi()
	'''

	def setupUi(self, Main):

		'''
		Função setupUi
		--------------
		Monta a pilha de telas

		Telas
		-----
		stack0 -> tela primeiro acesso
		stack1 -> tela inicial
		stack2 -> tela de login
		stack3 -> tela de opções para o funcionario
		stack4 -> tela para tipos de cadastro
		stack5 -> tela para opções de exclusão
		stack6 -> tela para opções de listagens
		stack7 -> tela para cadastro de funcionários
		stack8 -> tela para cadastro de clientes
		stack9 -> tela para cadastro de clientes
		stack10 -> tela para listar dados
		stack11 -> tela login cliente
		stack12 -> tela de vendas
		stack13 -> tela de validar
		'''
		Main.setObjectName('Main')
		Main.resize(640, 480)
	
		self.QtStack = QtWidgets.QStackedLayout()

		self.stack0 = QtWidgets.QMainWindow()
		self.stack1 = QtWidgets.QMainWindow()
		self.stack2 = QtWidgets.QMainWindow()
		self.stack3 = QtWidgets.QMainWindow()
		self.stack4 = QtWidgets.QMainWindow()
		self.stack5 = QtWidgets.QMainWindow()
		self.stack6 = QtWidgets.QMainWindow()
		self.stack7 = QtWidgets.QMainWindow()
		self.stack8 = QtWidgets.QMainWindow()
		self.stack9 = QtWidgets.QMainWindow()
		self.stack10 = QtWidgets.QMainWindow()
		self.stack11 = QtWidgets.QMainWindow()
		self.stack12 = QtWidgets.QMainWindow()
		self.stack13 = QtWidgets.QMainWindow()
		self.stack14 = QtWidgets.QMainWindow()
		self.stack15 = QtWidgets.QMainWindow()
		self.stack16 = QtWidgets.QMainWindow()
		self.stack17 = QtWidgets.QMainWindow()

		self.primeiro_acesso = Tela_primeiro_acesso()
		self.primeiro_acesso.setupUi(self.stack0)

		self.tela_inicial = Tela_inicial()
		self.tela_inicial.setupUi(self.stack1)

		self.tela_loginFunc = Tela_login_func()
		self.tela_loginFunc.setupUi(self.stack2)

		self.tela_op_funcionario = Tela_op_funcionario()
		self.tela_op_funcionario.setupUi(self.stack3)

		self.tela_tipo_cadastro = Tela_tipo_cadastro()
		self.tela_tipo_cadastro.setupUi(self.stack4)

		self.tela_tipo_exclusao = Tela_tipo_exclusao()
		self.tela_tipo_exclusao.setupUi(self.stack5)

		self.tela_listagens = Tela_listagens()
		self.tela_listagens.setupUi(self.stack6)

		self.tela_cadastro_funcionario = Tela_cadastro_funcionario()
		self.tela_cadastro_funcionario.setupUi(self.stack7)
		
		self.tela_cadastro_cliente = Tela_cadastro_cliente()
		self.tela_cadastro_cliente.setupUi(self.stack8)

		self.tela_cadastro_produto = Tela_cadastro_produto()
		self.tela_cadastro_produto.setupUi(self.stack9)

		self.tela_listDados = Tela_listDados()
		self.tela_listDados.setupUi(self.stack10)

		self.tela_login_cli = Tela_login_cli()
		self.tela_login_cli.setupUi(self.stack11)

		self.tela_vendas = Tela_vendas()
		self.tela_vendas.setupUi(self.stack12)

		self.tela_validar = Tela_validar()
		self.tela_validar.setupUi(self.stack13)

		self.telaListaFun = TelaListaFunc()
		self.telaListaFun.setupUi(self.stack14)

		self.telaListaCli = TelaListaCli()
		self.telaListaCli.setupUi(self.stack15)

		self.telaListaProd = TelaListProd()
		self.telaListaProd.setupUi(self.stack16)

		self.tela_primeiro_cad = Tela_primeiro_cad()
		self.tela_primeiro_cad.setupUi(self.stack17)

		self.QtStack.addWidget(self.stack0)#tela primeiro acesso
		self.QtStack.addWidget(self.stack1)#tela inicial
		self.QtStack.addWidget(self.stack2)#tela de login funcionario
		self.QtStack.addWidget(self.stack3)#tela de opções para o funcionario
		self.QtStack.addWidget(self.stack4)#tela para tipos de cadastro
		self.QtStack.addWidget(self.stack5)#tela para opções de exclusão
		self.QtStack.addWidget(self.stack6)#tela para opções de listagens
		self.QtStack.addWidget(self.stack7)#tela para cadastro de funcionários
		self.QtStack.addWidget(self.stack8)#tela para cadastro de clientes
		self.QtStack.addWidget(self.stack9)#tela para cadastro de produto
		self.QtStack.addWidget(self.stack10)#tela para listar dados
		self.QtStack.addWidget(self.stack11)#tela login cliente
		self.QtStack.addWidget(self.stack12)#tela de vendas
		self.QtStack.addWidget(self.stack13)#tela de validar
		self.QtStack.addWidget(self.stack14)#tela lista funcionario / excluir
		self.QtStack.addWidget(self.stack15)#tela lista Cliente / ecluir
		self.QtStack.addWidget(self.stack16)#tela lista de produto / excluir
		self.QtStack.addWidget(self.stack17)#tela cadastra primero acesso

		

class Main(QMainWindow, Ui_main):
	'''
	class Main()
	------------
	Responsavel por realizar a interação das telas

	Paramentros 
	-----------
	Ui_main -> Ui_main()

	Funções
	-------
	primeiro_cadastro()

	'''

	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.setupUi(self)

		# cadastro de cliete
		self.cadastra_cli = Cadastra_cli()

		# cadastro de funcionario
		self.cadastra_fun = Cadastra_func()

		# cadastro de produto
		self.cadastra_prod = Cadastra_prond()
		
		#Interação tela primeiro acesso
		self.primeiro_acesso.pushButton.clicked.connect(self.primeiro_cadastro)
		self.primeiro_acesso.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
		self.primeiro_acesso.pushButton_3.clicked.connect(lambda: self.QtStack.setCurrentIndex(17))

		self.tela_primeiro_cad.pushButton.clicked.connect(self.primeiroCadFunc)
		self.tela_primeiro_cad.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(0))
		
		# Interação tela inicial
		self.tela_inicial.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(2))
		self.tela_inicial.pushButton_2.clicked.connect(self.abrirLoginCli)
		self.tela_inicial.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit)

		# Interação tela login funcionario
		self.tela_loginFunc.pushButton.clicked.connect(self.btnLoginFunc)
		self.tela_loginFunc.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(1))

		#Interação tela login cliete
		# self.tela_login_cli.pushButton.clicked.connect(self.btnLoginCli)
		# self.tela_login_cli.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(1))
		
		#Interação tela de opções para o Funcionario
		self.tela_op_funcionario.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(4))#tipos de cadastro
		self.tela_op_funcionario.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(6))#tipos de listagem
		self.tela_op_funcionario.pushButton_4.clicked.connect(lambda: self.QtStack.setCurrentIndex(1))#voltar para login

		# Interação tela tipos de cadastro
		self.tela_tipo_cadastro.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(7))#cadastro de funcionarios
		self.tela_tipo_cadastro.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(8))#cadastro de clientes
		self.tela_tipo_cadastro.pushButton_3.clicked.connect(lambda: self.QtStack.setCurrentIndex(9))#cadastro de produto
		self.tela_tipo_cadastro.pushButton_4.clicked.connect(lambda: self.QtStack.setCurrentIndex(3))#voltar para tela de opções para funcionarios

		# Interação tela tipos de listagens		
		self.tela_listagens.pushButton.clicked.connect(self.btnListFunc)	
		self.tela_listagens.pushButton_2.clicked.connect(self.btnListCli)
		self.tela_listagens.pushButton_3.clicked.connect(self.btnListProd)		
		self.tela_listagens.pushButton_4.clicked.connect(lambda: self.QtStack.setCurrentIndex(3))

		# interação listar Func
		self.telaListaFun.pushButton_3.clicked.connect(lambda: self.QtStack.setCurrentIndex(6))

		# interaçãp listar Cli
		self.telaListaCli.pushButton_3.clicked.connect(lambda: self.QtStack.setCurrentIndex(6))

		# interaçãp listar prod
		self.telaListaProd.pushButton_3.clicked.connect(lambda: self.QtStack.setCurrentIndex(6))

		# Interação tela cadastra funcionario
		self.tela_cadastro_funcionario.pushButton.clicked.connect(self.btnCadastra_func)
		self.tela_cadastro_funcionario.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(4))

		# Interação tela cadastra cliente
		self.tela_cadastro_cliente.pushButton.clicked.connect(self.btnCadastra_cliente)
		self.tela_cadastro_cliente.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(4))

		# Interação tela cadastra produto
		self.tela_cadastro_produto.pushButton.clicked.connect(self.btnCadastra_prod)
		self.tela_cadastro_produto.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(4))


		# # Interação tela de vendas
		# self.tela_vendas.pushButton.clicked.connect(self.btnAddProd)
		# self.tela_vendas.pushButton_2.clicked.connect(self.btnRemoverProd)
		# self.tela_vendas.pushButton_3.clicked.connect(self.btnFinalizar_comp)
		# self.tela_vendas.pushButton_4.clicked.connect(lambda: self.QtStack.setCurrentIndex(1))

		# # Interação tela validar vendar
		# self.tela_validar.pushButton.clicked.connect(self.valida_compra)
		# self.tela_validar.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(13))

		# #Interação para excluir funcionário
		# self.tela_excluir_funcionario.pushButton_2.clicked.connect(self.btnExcFunc)
		# self.tela_excluir_funcionario.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(5))

		# #Interação para excluir clientes
		# self.tela_excluir_cliente.pushButton_2.clicked.connect(self.btnExcCliente)
		# self.tela_excluir_cliente.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(5))

		# #Interação para excluir produto
		# self.tela_excluir_produto.pushButton_2.clicked.connect(self.btnExcProd)
		# self.tela_excluir_produto.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(5))

	def primeiro_cadastro(self):
		'''
		primeiro_acesso()
		-------------------
		Define o primero funcionario do sistema, reliza o primero cadastro
		'''
		cpf = self.primeiro_acesso.lineEdit.text()
		senha = self.primeiro_acesso.lineEdit_2.text()

		if(not(cpf == '' or senha == '')):
			if(self.cadastra_fun.login(cpf, senha)):
				self.QtStack.setCurrentIndex(1)

			else:
				QMessageBox.information(None, 'Login','Usuario não cadastrado')	
				self.primeiro_acesso.lineEdit.setText('')
				self.primeiro_acesso.lineEdit_2.setText('')

		else:
			QMessageBox.information(None, 'Login', 'Informe todos os dados')
		
		

	
	def primeiroCadFunc(self):

		nome = self.tela_primeiro_cad.lineEdit.text()
		cpf = self.tela_primeiro_cad.lineEdit_2.text()
		salario = self.tela_primeiro_cad.lineEdit_3.text()
		pwd = self.tela_primeiro_cad.lineEdit_4.text()

		if(not(nome == '' or cpf == '' or salario == '' or pwd == '')):
			sala = float(salario)
			if(self.cadastra_fun.insere(nome, cpf, sala, pwd) == None):
				QMessageBox.information(None, 'Cadastro', 'Funcionário cadastrado com sucesso!')
				self.QtStack.setCurrentIndex(1)
				self.tela_primeiro_cad.lineEdit.setText('')
				self.tela_primeiro_cad.lineEdit_2.setText('')
				self.tela_primeiro_cad.lineEdit_3.setText('')
				self.tela_primeiro_cad.lineEdit_4.setText('')
			
			else:
				QMessageBox.information(None, 'Cadastro','Cpf informado, já cadastrado!')

		else:
			QMessageBox.information(None, 'Login', 'Informe todos os dados')
		


	def btnLoginFunc(self):
		'''
		btnLoginFunc()
		--------------
		Reliza a validação do funcionario

		Funções
		--------
		cadastra_funcionario.busca() 
		'''
	
		cpf = self.tela_loginFunc.lineEdit.text()
		senha = self.tela_loginFunc.lineEdit_2.text()

		if(not(cpf == '' or senha == '')):
			if(self.cadastra_fun.login(cpf, senha)):
				self.QtStack.setCurrentIndex(3)

			else:
				QMessageBox.information(None, 'Login','Usuario não cadastrado')	
				

		else:
			QMessageBox.information(None, 'Login', 'Informe todos os dados')

		self.tela_loginFunc.lineEdit.setText('')
		self.tela_loginFunc.lineEdit_2.setText('')
	
	def abrirLoginCli(self):
		
		'''
		abrirLoginCli()
		---------------
		Define qual ação o cliente poderá realizar
		'''

		if(self.cadastra_cliente.lista_pessoas != []):

			if(self.cadastra_produto.lista_produtos != []):
				self.tela_vendas.listWidget_2.clear()

				self.tela_vendas.lineEdit_3.setText('')

				for qtd, prod in  enumerate(self.cadastra_produto.lista_produtos):
					info = "Produto: {}\nCódigo: {}\nNome: {}\nValor: {}\nQuantidade: {}\n" \
					.format(qtd+1, prod.codigo, prod.nome, prod.valor, prod.quantidade)
					self.tela_vendas.listWidget.addItem(info)

				self.tela_vendas.listWidget_2.clear()
				self.QtStack.setCurrentIndex(11)
				# Realiza vendas 
				self.vendas = Vendas(self.cadastra_produto.lista_produtos)
			else:
				QMessageBox.information(None, 'Login', 'Não existem produtos cadastrados')
			
		else:
			QMessageBox.information(None, 'Login', 'Não existem clientes cadastrados')
		
	def btnLoginCli(self):
		'''
		btnLoginCli()
		-------------
		Define se a tela de login séra aberta
		''' 

		cpf = self.tela_login_cli.lineEdit.text()
		self.tela_vendas.lineEdit_3.setText('')
		
		if(not(cpf == '')):
			exite = self.cadastra_cliente.busca(cpf)

			if(exite != None):
				self.QtStack.setCurrentIndex(12)
				

			else:
				QMessageBox.information(None, 'Login', 'Cpf não encotrado')
				self.tela_login.lineEdit.setText('')

		else:
			QMessageBox.information(None, 'Login', 'Informe seu cpf')
	
	def btnCadastra_func(self):
		'''
		btnCadastra_func()
		------------------
		Cadastra funcionario criado um objeto do tipo Funcionario e
		adiciona na lista de funcionario
		'''

		nome = self.tela_cadastro_funcionario.lineEdit.text()
		cpf = self.tela_cadastro_funcionario.lineEdit_2.text()
		salario = self.tela_cadastro_funcionario.lineEdit_3.text()
		pwd = self.tela_cadastro_funcionario.lineEdit_4.text()

		if(not(nome == '' or cpf == '' or salario == '' or pwd == '')):
			sala = float(salario)
			if(self.cadastra_fun.insere(nome, cpf, sala, pwd) == None):
				QMessageBox.information(None, 'Cadastro', 'Funcionário cadastrado com sucesso!')
				self.tela_cadastro_funcionario.lineEdit.setText('')
				self.tela_cadastro_funcionario.lineEdit_2.setText('')
				self.tela_cadastro_funcionario.lineEdit_3.setText('')
				self.tela_cadastro_funcionario.lineEdit_4.setText('')
			
			else:
				QMessageBox.information(None, 'Cadastro','Cpf informado, já cadastrado!')

		else:
			QMessageBox.information(None, 'Login', 'Informe todos os dados')

	def btnCadastra_cliente(self):
		'''
		btnCadastra_cliente()
		---------------------
		Cadastra Pessoa criado um objeto do tipo Pessoa e
		adiciona na lista de Pessoa
		'''

		nome = self.tela_cadastro_cliente.lineEdit.text()
		cpf = self.tela_cadastro_cliente.lineEdit_2.text()

		if(not(nome == '' or cpf == '')):
		
			if(self.cadastra_cli.insere(nome, cpf) == None):
				QMessageBox.information(None, 'Cadastro', 'Cliete cadastrado com sucesso!')
				self.tela_cadastro_cliente.lineEdit.setText('')
				self.tela_cadastro_cliente.lineEdit_2.setText('')
			
			else:
				QMessageBox.information(None, 'Cadastro','Cpf informado, já cadastrado!')

		else:
			QMessageBox.information(None, 'Login', 'Informe todos os dados')
	
	def btnCadastra_prod(self):
		'''
		btnCadastra_cliente()
		---------------------
		Cadastra Produto criado um objeto do tipo Produto e
		adiciona na lista de Produto
		'''
		nome = self.tela_cadastro_produto.lineEdit.text()
		valor = self.tela_cadastro_produto.lineEdit_2.text()
		quantidade = self.tela_cadastro_produto.lineEdit_3.text()

		if(not(nome == '' or valor == '' or quantidade == '')):
			preco = float(valor)
			qtd = int(quantidade)
			self.cadastra_prod.insere(nome, preco, qtd)

			self.tela_cadastro_produto.lineEdit.setText('')
			self.tela_cadastro_produto.lineEdit_2.setText('')
			self.tela_cadastro_produto.lineEdit_3.setText('')

			QMessageBox.information(None, 'Cadastro', 'Cadastro realizado com sucesso!')
		else:
			QMessageBox.information(None, 'Cadastro', 'Informe todos os dados')

	def btnListFunc(self):
		resp = self.cadastra_fun.imprimir()

		self.telaListaFun.tableWidget.setRowCount(len(resp))
		self.telaListaFun.tableWidget.setColumnCount(3)

		for i in range(0, len(resp)):
			for j in range(0, 3):
				self.telaListaFun.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resp[i][j])))
		
		self.QtStack.setCurrentIndex(14)


	def btnListCli(self):

		resp = self.cadastra_cli.imprimir()

		self.telaListaCli.tableWidget.setRowCount(len(resp))
		self.telaListaCli.tableWidget.setColumnCount(2)

		for i in range(0, len(resp)):
			for j in range(0, 2):
				self.telaListaCli.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resp[i][j])))
		
		self.QtStack.setCurrentIndex(15)

	def btnListProd(self):

		resp = self.cadastra_prod.imprimir()

		self.telaListaProd.tableWidget.setRowCount(len(resp))
		self.telaListaProd.tableWidget.setColumnCount(4)

		for i in range(0, len(resp)):
			for j in range(0, 4):
				self.telaListaProd.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resp[i][j])))
		
		self.QtStack.setCurrentIndex(16)

	
	# Vendas
	# def btnAddProd(self):
	# 	'''
	# 	btnAddProd()
	# 	------------
	# 	Ações de vendas, trabalha com as funções da classe Venda

	# 	'''
	# 	codigo = self.tela_vendas.lineEdit.text()
	# 	quantidade = self.tela_vendas.lineEdit_2.text()


	# 	if(codigo != '' or quantidade != ''):
	# 		produto = self.cadastra_produto.busca(codigo)
			
	# 		if(produto != None and produto.quantidade > 0):
	# 			qtd = int(quantidade)
				
	# 			if(self.vendas.add_produto(produto, qtd)):
	# 				self.qtdAux.append(qtd)

	# 				self.tela_vendas.listWidget_2.clear()

	# 				self.tela_vendas.lineEdit_3.setText('')
	# 				self.tela_vendas.lineEdit_3.setText(str(self.vendas.total))
				
	# 				self.tela_vendas.listWidget_2.clear()
	# 				for qtd, prod in  enumerate(self.vendas.lista_compras):
	# 					info = "Produto: {}\nCódigo: {}\nNome: {}\nValor: {}\nQuantidade: {}\n" \
	# 					.format(qtd+1, prod.codigo, prod.nome, prod.valor, prod.quantidade)
						
	# 					self.tela_vendas.listWidget_2.addItem(info)
						
					
	# 				self.tela_vendas.listWidget.clear()
	# 				zerado = True
	# 				for qtd, prod in  enumerate(self.cadastra_produto.lista_produtos):
	# 					if(prod.quantidade > 0):
	# 						info = "Produto: {}\nCódigo: {}\nNome: {}\nValor: {}\nQuantidade: {}\n" \
	# 						.format(qtd+1, prod.codigo, prod.nome, prod.valor, prod.quantidade)
	# 						self.tela_vendas.listWidget.addItem(info)
	# 						zerado = False
						
	# 				if(zerado):
	# 					QMessageBox.information(None, 'Vendas', 'Estoque zerado')

					
	# 			else:
	# 				QMessageBox.information(None, 'Vendas', 'Quantidade invalida')

	# 		else:
	# 			QMessageBox.information(None, 'Vendas', 'Produto não existe')

	# 	else:
	# 		QMessageBox.information(None, 'Vendas', 'Preencha todos os Dados')
		
	# 	self.tela_vendas.lineEdit.setText('')
	# 	self.tela_vendas.lineEdit_2.setText('')

	# def btnRemoverProd(self):
		
	# 	lista = self.tela_vendas.listWidget_2.selectedItems()

	# 	if(self.vendas.lista_compras != []):
	# 			if(lista != []):
	# 				#self.tela_vendas.listWidget_2.clear()
	# 				self.tela_vendas.lineEdit_3.setText('')

	# 				if not lista:
	# 					return
	# 				for itm in lista:
	# 					indice = self.tela_vendas.listWidget_2.row(itm)
	# 					self.tela_vendas.listWidget_2.takeItem(self.tela_vendas.listWidget_2.row(itm))

	# 				self.vendas.total -= self.vendas.lista_compras[indice].valor * self.qtdAux[indice]
					
	# 				cod = self.vendas.lista_compras[indice].codigo
	# 				for i in self.cadastra_produto.lista_produtos:
	# 					if(i.codigo == cod):
	# 						i.quantidade += self.qtdAux[indice]
	# 				del(self.vendas.lista_compras[indice])
	# 				del(self.qtdAux[indice])

	# 				self.tela_vendas.lineEdit_3.setText('')
	# 				self.tela_vendas.lineEdit_3.setText(str(self.vendas.total))

	# 				self.tela_vendas.listWidget_2.clear()
	# 				for qtd, prod in  enumerate(self.vendas.lista_compras):
	# 					info = "Produto: {}\nCódigo: {}\nNome: {}\nValor: {}\nQuantidade: {}\n" \
	# 					.format(qtd+1, prod.codigo, prod.nome, prod.valor, prod.quantidade)
	# 					self.tela_vendas.listWidget_2.addItem(info)

	# 				self.tela_vendas.listWidget.clear()
	# 				for qtd, prod in  enumerate(self.cadastra_produto.lista_produtos):		
	# 					info = "Produto: {}\nCódigo: {}\nNome: {}\nValor: {}\nQuantidade: {}\n" \
	# 					.format(qtd+1, prod.codigo, prod.nome, prod.valor, prod.quantidade)
	# 					self.tela_vendas.listWidget.addItem(info)
	# 			else:
	# 				QMessageBox.information(None, 'Vendas', 'Nenhum item selecionado!')
		
	# 	else:
	# 		QMessageBox.information(None, 'Vendas', 'Lista de compras vazia!')
		
	# def btnFinalizar_comp(self):
	# 	'''
	# 	btnFinalizar_comp()
	# 	-------------------
	# 	Responsavel por redirecionar o usuario quando a compra for finalizada 

	# 	'''

	# 	if(self.vendas.lista_compras != []):
	# 		self.QtStack.setCurrentIndex(13)
	# 	else:
	# 		QMessageBox.information(None, 'Vendas', 'Adicione algum produto no carrilho')

	# def valida_compra(self):

	# 	'''
	# 	valida_compra()
	# 	---------------
	# 	Buca por um funcionario, antes da compra ser finalida
	# 	'''

	# 	cpf = self.tela_validar.lineEdit.text()

	# 	if(cpf != ''):
	# 		existe = self.cadastra_funcionario.busca(cpf)

	# 		if(existe != None):
	# 			QMessageBox.information(None, 'Vendas', 'Compra concluida')
	# 			self.tela_validar.lineEdit.setText('')
	# 			self.cadastra_produto.rm_prod_zerado()
	# 			self.QtStack.setCurrentIndex(1)
			
	# 		else:
	# 			QMessageBox.information(None, 'Vendas', 'Funcionario não encontrado')
	# 			cpf = self.tela_validar.lineEdit.setText('')

	# 	else:
	# 		QMessageBox.information(None, 'Vendas', 'Preencha todos os Dados')

	# def btnExcFunc(self):
	# 	cpf = self.tela_excluir_funcionario.lineEdit.text()
	# 	self.tela_excluir_funcionario.lineEdit.setText('')
	# 	if(cpf != ''):
	# 		funcionario = self.cadastra_funcionario.busca(cpf)
	# 		if(funcionario != None):
	# 			self.cadastra_funcionario.lista_pessoas.remove(funcionario)
	# 			self.tela_excluir_funcionario.lineEdit.setText('')
	# 			QMessageBox.information(None,'Excluir', 'Funcinário Excluido')
	# 		else:
	# 			QMessageBox.information(None,'Excluir', 'Funcinário não encontrado!')
	# 	else:
	# 		QMessageBox.information(None, 'Excluir', 'Campo obrigatório!')

	# def btnExcCliente(self):
	# 	cpf = self.tela_excluir_cliente.lineEdit.text()

	# 	if(cpf != ''):
	# 		cliente = self.cadastra_cliente.busca(cpf)
	# 		if(cliente != None):
	# 			self.cadastra_cliente.lista_pessoas.remove(cliente)
	# 			self.tela_excluir_cliente.lineEdit.setText('')
	# 			QMessageBox.information(None, 'Excluir', 'Cliente excluido do cadastro')
	# 		else:
	# 			QMessageBox.information(None,'Excluir', 'Cliente não encontrado!')
	# 	else:
	# 		QMessageBox.information(None, 'Excluir', 'Campo obrigatório!')

	# def btnExcProd(self):
	# 	cod = self.tela_excluir_produto.lineEdit.text()

	# 	if(cod != ''):
	# 		codigo = self.cadastra_produto.busca(cod)
	# 		if(codigo != None):
	# 			self.cadastra_produto.lista_produtos.remove(codigo)
	# 			self.tela_excluir_cliente.lineEdit.setText('')
	# 			QMessageBox.information(None, 'Excluir', 'Produto excluido do estoque')
	# 		else:
	# 			QMessageBox.information(None,'Excluir', 'Produto não encontrado!')
	# 	else:
	# 		QMessageBox.information(None, 'Excluir', 'Campo obrigatório!')



if __name__ == "__main__":
	app = QApplication(sys.argv)
	show_main = Main()
	sys.exit(app.exec_())
	Main.close()
