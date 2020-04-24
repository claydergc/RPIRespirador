# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(800, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Principal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(200, 50, 200, 50)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.btnAjustes = QtWidgets.QPushButton(Principal)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btnAjustes.setFont(font)
        self.btnAjustes.setObjectName("btnAjustes")
        self.gridLayout.addWidget(self.btnAjustes, 2, 0, 1, 1)
        self.btnVentAsistida = QtWidgets.QPushButton(Principal)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btnVentAsistida.setFont(font)
        self.btnVentAsistida.setObjectName("btnVentAsistida")
        self.gridLayout.addWidget(self.btnVentAsistida, 1, 0, 1, 1)
        self.btnVentControlada = QtWidgets.QPushButton(Principal)
        self.btnVentControlada.setSizeIncrement(QtCore.QSize(0, 0))
        self.btnVentControlada.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.btnVentControlada.setFont(font)
        self.btnVentControlada.setIconSize(QtCore.QSize(16, 16))
        self.btnVentControlada.setObjectName("btnVentControlada")
        self.gridLayout.addWidget(self.btnVentControlada, 0, 0, 1, 1)
        self.btnCalibrar = QtWidgets.QPushButton(Principal)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btnCalibrar.setFont(font)
        self.btnCalibrar.setObjectName("btnCalibrar")
        self.gridLayout.addWidget(self.btnCalibrar, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Form"))
        self.btnAjustes.setText(_translate("Principal", "Ajustes"))
        self.btnVentAsistida.setText(_translate("Principal", "Ventilación Asistida"))
        self.btnVentControlada.setText(_translate("Principal", "Ventilación Controlada"))
        self.btnCalibrar.setText(_translate("Principal", "Calibrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QWidget()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())

