# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class MainShutdownForm(object):
    def setupUi(self, MainShutdownForm):
        if not MainShutdownForm.objectName():
            MainShutdownForm.setObjectName(u"MainShutdownForm")
        MainShutdownForm.resize(284, 132)
        MainShutdownForm.setMaximumSize(QSize(284, 132))
        icon = QIcon()
        icon.addFile(u"./assets/icons/power-off.png", QSize(), QIcon.Normal, QIcon.Off)
        MainShutdownForm.setWindowIcon(icon)
        self.botonApagar = QPushButton(MainShutdownForm)
        self.botonApagar.setObjectName(u"botonApagar")
        self.botonApagar.setGeometry(QRect(100, 90, 75, 24))
        self.label = QLabel(MainShutdownForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 221, 16))
        font = QFont()
        font.setFamilies([u"Roboto Black"])
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.spinHoras = QSpinBox(MainShutdownForm)
        self.spinHoras.setObjectName(u"spinHoras")
        self.spinHoras.setGeometry(QRect(30, 50, 42, 22))
        self.spinHoras.setMaximum(99)
        self.label_2 = QLabel(MainShutdownForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(34, 30, 31, 16))
        self.label_3 = QLabel(MainShutdownForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 30, 51, 20))
        self.spinMinutos = QSpinBox(MainShutdownForm)
        self.spinMinutos.setObjectName(u"spinMinutos")
        self.spinMinutos.setGeometry(QRect(120, 50, 42, 22))
        self.spinMinutos.setMaximum(59)
        self.spinSegundos = QSpinBox(MainShutdownForm)
        self.spinSegundos.setObjectName(u"spinSegundos")
        self.spinSegundos.setGeometry(QRect(204, 50, 42, 22))
        self.spinSegundos.setMaximum(60)
        self.label_4 = QLabel(MainShutdownForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 30, 51, 20))

        self.retranslateUi(MainShutdownForm)

        QMetaObject.connectSlotsByName(MainShutdownForm)
    # setupUi

    def retranslateUi(self, MainShutdownForm):
        MainShutdownForm.setWindowTitle(QCoreApplication.translate("MainShutdownForm", u"Apagador", None))
        self.botonApagar.setText(QCoreApplication.translate("MainShutdownForm", u"Apagar", None))
        self.label.setText(QCoreApplication.translate("MainShutdownForm", u"Elige el tiempo para apagar la PC:", None))
        self.label_2.setText(QCoreApplication.translate("MainShutdownForm", u"Horas", None))
        self.label_3.setText(QCoreApplication.translate("MainShutdownForm", u"Minutos", None))
        self.label_4.setText(QCoreApplication.translate("MainShutdownForm", u"Segundos", None))
    # retranslateUi

