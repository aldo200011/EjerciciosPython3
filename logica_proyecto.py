from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication
from PySide2.QtCore import Slot
from ui_proyecto import Ui_MainWindow
from Proyecto.estudiante import Estudiante
import socket as s
import pickle
import time

class MainWindow(QMainWindow):
    cliente: s
    file = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.conectarButton.clicked.connect(self.conectar)
        self.ui.enviarEButton.clicked.connect(self.enviarEstudiante)
        self.ui.buscarButton.clicked.connect(self.abrirArchivo)
        self.ui.enviarAButton.clicked.connect(self.enviarArchivo)


    @Slot()
    def conectar(self):
        self.cliente = s.socket()

        if self.ui.estadoLabel.text() == 'Estado: Desconectado' and self.ui.conectarButton.text() == 'Conectar':
            self.ui.estadoLabel.setText('Estado: Conectado')
            self.ui.conectarButton.setText('Desconectar')
            self.cliente.connect((self.ui.ipLineEdit.text(), int(self.ui.puertoLineEdit.text())))
        else:
            self.ui.estadoLabel.setText('Estado: Desconectado')
            self.ui.conectarButton.setText('Conectar')
            self.cliente.close()


    @Slot()
    def enviarEstudiante(self):
        e = Estudiante(self.ui.nombreLineEdit.text(), self.ui.correoLineEdit.text(),
                                self.ui.contraseniaLineEdit.text())
        print(e.__str__())
        bin = pickle.dumps(e)
        self.cliente.send(bin)


    @Slot()
    def abrirArchivo(self):
        filename = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'Zip Files(*.zip)')
        self.file = open(filename[0], 'rb')
        self.ui.buscarLineEdit.setText(filename[0])


    @Slot()
    def enviarArchivo(self):
        f2 = open('AldoC.zip', 'wb')
        mensaje = 'iniciozip'
        bytes = mensaje.encode()
        self.cliente.send(bytes)
        chunk = self.file.read(500)

        while chunk:
            f2.write(chunk)
            self.cliente.send(f2)
            chunk = self.file.read(500)
            time.sleep(0.5)

        mensaje = 'finzip'
        bytes = mensaje.encode()
        self.cliente.send(bytes)
        f2.close()
        self.file.close()