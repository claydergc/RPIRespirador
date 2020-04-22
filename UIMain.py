# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIMain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.UIPrincipal import *
from ui.UIRespiracionControlada import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        #objeto de clase Ui_Principal
        self.form = QtWidgets.QWidget()
        self.uiPrincipal = Ui_Principal()
        self.uiPrincipal.setupUi(self.form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form.sizePolicy().hasHeightForWidth())
        self.form.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.form)
        #objeto de clase Ui_Principal

        #objeto de clase Ui_RespiracionControlada
        self.form2 = QtWidgets.QWidget()
        self.uiRespiracionControlada = Ui_RespiracionControlada()
        self.uiRespiracionControlada.setupUi(self.form2)
	#objeto de clase Ui_RespiracionControlada


        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.btnContinuar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnContinuar.sizePolicy().hasHeightForWidth())
        self.btnContinuar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnContinuar.setFont(font)
        self.btnContinuar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnContinuar.setObjectName("btnContinuar")
        self.horizontalLayout_2.addWidget(self.btnContinuar)
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRegresar.sizePolicy().hasHeightForWidth())
        self.btnRegresar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnRegresar.setObjectName("btnRegresar")
        self.horizontalLayout_2.addWidget(self.btnRegresar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.uiPrincipal.btnVentControlada.clicked.connect(self.gotoUIRespiracionControlada)
        self.btnRegresar.clicked.connect(self.gotoUIPrincipal)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnContinuar.setText(_translate("MainWindow", "Continuar"))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar"))

    def gotoUIRespiracionControlada(self):
        #self.uiPrincipal.pushButton.setText("Acabas de hacer clic en el boton!")
        self.verticalLayout.removeWidget(self.form)
        self.verticalLayout.update()
        self.form.setParent(None)
	#objeto de clase Ui_Principal
        #self.form2 = QtWidgets.QWidget()
        #self.uiRespiracionControlada = Ui_RespiracionControlada()
        #self.uiRespiracionControlada.setupUi(self.form2)
        #self.form2.setParent(self)        
        self.verticalLayout.addWidget(self.form2)
        #self.horizontalLayout.addWidget(self.Form, self.Form2)
        #objeto de clase Ui_Principal

    def gotoUIPrincipal(self):
        #self.uiPrincipal.pushButton.setText("Acabas de hacer clic en el boton!")
        self.verticalLayout.removeWidget(self.form2)
        self.verticalLayout.update()
        self.form2.setParent(None)
	#objeto de clase Ui_Principal
        #self.form = QtWidgets.QWidget()
        #self.uiPrincipal = Ui_Principal()
        #self.uiPrincipal.setupUi(self.form)
        self.verticalLayout.addWidget(self.form)
        #self.horizontalLayout.addWidget(self.Form, self.Form2)
        #objeto de clase Ui_Principal



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

