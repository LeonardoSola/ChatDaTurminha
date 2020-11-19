from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys

class Chat(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MainWindow")
        self.setFixedSize(500, 506)

        self.setStyleSheet("font-family: \"Gill Sans Extrabold\", Helvetica, sans-serif;")
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnEnviar = QPushButton(self.centralwidget)
        self.btnEnviar.setStyleSheet("font-size: 15px")
        self.btnEnviar.setObjectName("btnEnviar")
        self.gridLayout.addWidget(self.btnEnviar, 1, 2, 1, 1)
        self.mensagens = QTextEdit(self.centralwidget)
        self.mensagens.setStyleSheet("border-radius: 10px; background-color: white; font-size: 12pt")
        self.mensagens.setObjectName("mensagens")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 437))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout.addWidget(self.mensagens, 0, 0, 1, 3)
        self.inputMensagem = QLineEdit(self.centralwidget)
        self.inputMensagem.setMinimumSize(QtCore.QSize(0, 20))
        self.inputMensagem.setStyleSheet("font-size: 15px;")
        self.inputMensagem.setObjectName("inputMensagem")
        self.gridLayout.addWidget(self.inputMensagem, 1, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.actionConfig = QAction(self)
        self.actionConfig.setObjectName("actionConfig")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Turminha Chat"))
        self.btnEnviar.setText(_translate("MainWindow", "Enviar"))
        self.inputMensagem.setPlaceholderText("Digite um nome!")
        self.actionConfig.setText(_translate("MainWindow", "Config"))