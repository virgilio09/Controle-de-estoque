# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_primeiro_acesso(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(640, 480)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(270, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(260, 130, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(260, 190, 67, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(260, 150, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 210, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(260, 260, 71, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Login)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 440, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Login)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 440, 151, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Login)
        self.label_4.setGeometry(QtCore.QRect(340, 400, 271, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Login"))
        self.label_2.setText(_translate("Login", "CPF:"))
        self.label_3.setText(_translate("Login", "Senha:"))
        self.pushButton.setText(_translate("Login", "Entrar"))
        self.pushButton_2.setText(_translate("Login", "Sair"))
        self.pushButton_3.setText(_translate("Login", "Novo cadastro"))
        self.label_4.setText(_translate("Login", "Não possuí cadastro? realize um novo"))
