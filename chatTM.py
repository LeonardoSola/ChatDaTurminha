import requests
import json
from design import *

class ChatTM(Chat):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.url = ''
        self.nome = False
        self.historico = {}
        self.timer = QtCore.QBasicTimer()

        self.inputMensagem.returnPressed.connect(self.enviar)
        self.btnEnviar.clicked.connect(self.enviar)

    def input_nome(self):
        nome = self.inputMensagem.text()
        if nome.__len__() >= 3 and nome.__len__() <= 10:
            self.nome = nome.upper()
            self.inputMensagem.setPlaceholderText("Digite URL do server!")
            self.inputMensagem.setText('')
        else:
            self.inputMensagem.setText('')
            self.inputMensagem.setPlaceholderText("Nome precisa ter mais de 3 letras e menos de 10!")


    def input_url(self):
        url = self.inputMensagem.text()
        self.url = url
        self.inputMensagem.setPlaceholderText("Digite Aqui!")
        self.inputMensagem.setText('')

        self.timer.start(100, self)


    def timerEvent(self,e):
        self.mostrar_mensagens()
        try:
            rget = requests.get(self.url)
            self.historico = rget.json()
        except:
            self.mensagens.setText('URL INVALIDA')
            self.historico = {}
    
    def enviar(self):
        if not self.nome:
            self.input_nome()
            return
        if not self.url:
            self.input_url()
            return
        if self.inputMensagem.text().startswith('config.mudar.server.pra='):
            novo_url = self.inputMensagem.text()
            self.url = novo_url[24:]
            print('novo url '+ self.url)
            return

        mensagem = self.inputMensagem.text()
        self.inputMensagem.setText('')

        mensagem =  {'user': self.nome, 'message': mensagem}
        headers = {'content-type': 'application/json'}
        try:
            requests.post(self.url, data=json.dumps(mensagem), headers=headers)
        except:
            self.mensagens.setText('URL INVALIDA')
        self.mostrar_mensagens()

    def mostrar_mensagens(self):
        novos = ''
        for x,y in self.historico.items():
            novos+= f'[{y["user"]}]: {y["message"]}\n'
        self.mensagens.setText(novos)
        self.mensagens.moveCursor(QtGui.QTextCursor.End)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    chat = ChatTM()
    chat.show()
    sys.exit(qt.exec_())