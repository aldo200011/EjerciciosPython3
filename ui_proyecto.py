# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyecto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(370, 391)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.servidorGBox = QGroupBox(self.centralwidget)
        self.servidorGBox.setObjectName(u"servidorGBox")
        self.servidorGBox.setGeometry(QRect(0, 0, 371, 91))
        font = QFont()
        font.setPointSize(10)
        self.servidorGBox.setFont(font)
        self.ipLabel = QLabel(self.servidorGBox)
        self.ipLabel.setObjectName(u"ipLabel")
        self.ipLabel.setGeometry(QRect(10, 30, 21, 16))
        self.ipLineEdit = QLineEdit(self.servidorGBox)
        self.ipLineEdit.setObjectName(u"ipLineEdit")
        self.ipLineEdit.setGeometry(QRect(40, 30, 113, 21))
        self.puertoLabel = QLabel(self.servidorGBox)
        self.puertoLabel.setObjectName(u"puertoLabel")
        self.puertoLabel.setGeometry(QRect(200, 30, 41, 16))
        self.puertoLineEdit = QLineEdit(self.servidorGBox)
        self.puertoLineEdit.setObjectName(u"puertoLineEdit")
        self.puertoLineEdit.setGeometry(QRect(250, 30, 113, 21))
        self.conectarButton = QPushButton(self.servidorGBox)
        self.conectarButton.setObjectName(u"conectarButton")
        self.conectarButton.setGeometry(QRect(10, 60, 351, 22))
        self.estudianteGBox = QGroupBox(self.centralwidget)
        self.estudianteGBox.setObjectName(u"estudianteGBox")
        self.estudianteGBox.setGeometry(QRect(0, 100, 371, 151))
        self.estudianteGBox.setFont(font)
        self.nombreLabel = QLabel(self.estudianteGBox)
        self.nombreLabel.setObjectName(u"nombreLabel")
        self.nombreLabel.setGeometry(QRect(10, 30, 51, 16))
        self.nombreLineEdit = QLineEdit(self.estudianteGBox)
        self.nombreLineEdit.setObjectName(u"nombreLineEdit")
        self.nombreLineEdit.setGeometry(QRect(90, 30, 271, 21))
        self.correoLineEdit = QLineEdit(self.estudianteGBox)
        self.correoLineEdit.setObjectName(u"correoLineEdit")
        self.correoLineEdit.setGeometry(QRect(90, 60, 271, 21))
        self.contraseniaLineEdit = QLineEdit(self.estudianteGBox)
        self.contraseniaLineEdit.setObjectName(u"contraseniaLineEdit")
        self.contraseniaLineEdit.setGeometry(QRect(90, 90, 271, 21))
        self.correoLabel = QLabel(self.estudianteGBox)
        self.correoLabel.setObjectName(u"correoLabel")
        self.correoLabel.setGeometry(QRect(10, 60, 47, 14))
        self.contraseniaLabel = QLabel(self.estudianteGBox)
        self.contraseniaLabel.setObjectName(u"contraseniaLabel")
        self.contraseniaLabel.setGeometry(QRect(10, 90, 71, 16))
        self.enviarEButton = QPushButton(self.estudianteGBox)
        self.enviarEButton.setObjectName(u"enviarEButton")
        self.enviarEButton.setGeometry(QRect(10, 120, 351, 22))
        self.archivoGBox = QGroupBox(self.centralwidget)
        self.archivoGBox.setObjectName(u"archivoGBox")
        self.archivoGBox.setGeometry(QRect(0, 260, 371, 91))
        self.archivoGBox.setFont(font)
        self.buscarButton = QPushButton(self.archivoGBox)
        self.buscarButton.setObjectName(u"buscarButton")
        self.buscarButton.setGeometry(QRect(10, 30, 80, 22))
        self.buscarLineEdit = QLineEdit(self.archivoGBox)
        self.buscarLineEdit.setObjectName(u"buscarLineEdit")
        self.buscarLineEdit.setGeometry(QRect(100, 30, 261, 21))
        self.enviarAButton = QPushButton(self.archivoGBox)
        self.enviarAButton.setObjectName(u"enviarAButton")
        self.enviarAButton.setGeometry(QRect(10, 60, 351, 22))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 360, 371, 31))
        self.estadoLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.estadoLayout.setObjectName(u"estadoLayout")
        self.estadoLayout.setContentsMargins(0, 0, 0, 0)
        self.estadoLabel = QLabel(self.horizontalLayoutWidget)
        self.estadoLabel.setObjectName(u"estadoLabel")
        self.estadoLabel.setFont(font)

        self.estadoLayout.addWidget(self.estadoLabel, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cliente Aldo", None))
        self.servidorGBox.setTitle(QCoreApplication.translate("MainWindow", u"Servidor", None))
        self.ipLabel.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.puertoLabel.setText(QCoreApplication.translate("MainWindow", u"Puerto:", None))
        self.conectarButton.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.estudianteGBox.setTitle(QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.nombreLabel.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.correoLabel.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.contraseniaLabel.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.enviarEButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.archivoGBox.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.buscarButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.enviarAButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.estadoLabel.setText(QCoreApplication.translate("MainWindow", u"Estado: Desconectado", None))
    # retranslateUi

