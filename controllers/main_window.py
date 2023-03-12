from PySide6.QtWidgets import QWidget, QMessageBox
from views.main_window import MainShutdownForm
from PySide6 import QtGui
from os import system

class MainShutdownWindow(QWidget, MainShutdownForm):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.botonApagar.clicked.connect(self.apagar)

    def apagar(self):
        horas = (self.spinHoras.value()) * 3600
        minutos = (self.spinMinutos.value()) * 60
        segundos = self.spinSegundos.value()

        tiempoTotal = horas + minutos + segundos

        system("shutdown -s -t " + str(tiempoTotal))

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Se apagará el PC")
        msgBox.setWindowIcon(QtGui.QIcon(u"./assets/icons/warning-sign.png"))
        msgBox.setText("Se ha iniciado la cuenta atras para apagar el PC.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        ventana = msgBox.exec()

        if ventana == QMessageBox.Ok:
            self.close()
        
        """ if (horas == 0) and (minutos == 0) and (segundos == 0):
            msgBox = QMessageBox()
            msgBox.setWindowTitle("ERROR")
            msgBox.setWindowIcon(QtGui.QIcon(u"./assets/icons/warning-sign.png"))
            msgBox.setText("No se puede programar para")
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Se apagará el PC")
            msgBox.setText("Se ha iniciado la cuenta atras para apagar el PC.")
            msgBox.exec() """