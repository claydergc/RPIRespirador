# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIMain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.UIPrincipal import *
from ui.UIRespiracionControlada import *
from ui.UIRespiracionAsistida import *
from ui.UIGraficas import *
from ui.UIAjustes import *
from ui.UIMaxMinParametros import *

class Ui_MainWindow(object):

    PANT_INICIAL = 0
    PANT_RESP_CONTROLADA = 1
    PANT_RESP_ASISTIDA = 2 
    PANT_AJUSTES = 3
    PANT_GRAFICAS = 4
    PANT_AJUSTES = 5
    PANT_MAXMINPARAMETROS = 6
    pantallaActual = PANT_INICIAL
    pantallaAnterior = PANT_INICIAL

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

        #objeto de clase Ui_RespiracionAsistida
        self.form3 = QtWidgets.QWidget()
        self.uiRespiracionAsistida = Ui_RespiracionAsistida()
        self.uiRespiracionAsistida.setupUi(self.form3)
	#objeto de clase Ui_RespiracionAsistida

	#objeto de clase Ui_Graficas
        self.form4 = QtWidgets.QWidget()
        self.uiGraficas = Ui_Graficas()
        self.uiGraficas.setupUi(self.form4)
	#objeto de clase Ui_Graficas

	#objeto de clase Ui_Graficas
        self.form5 = QtWidgets.QWidget()
        self.uiAjustes = Ui_Ajustes()
        self.uiAjustes.setupUi(self.form5)
	#objeto de clase Ui_Graficas

	#objeto de clase Ui_Graficas
        self.form6 = QtWidgets.QWidget()
        self.uiMaxMinParametros = Ui_MaxMinParametros()
        self.uiMaxMinParametros.setupUi(self.form6)
	#objeto de clase Ui_Graficas

        #self.widget = QtWidgets.QWidget(self.centralwidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        #self.widget.setSizePolicy(sizePolicy)
        #self.widget.setObjectName("widget")
        #self.verticalLayout.addWidget(self.widget)
        
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
        self.uiPrincipal.btnVentAsistida.clicked.connect(self.gotoUIRespiracionAsistida)
        self.uiPrincipal.btnAjustes.clicked.connect(self.gotoUIAjustes)
        #self.btnRegresar.clicked.connect(self.gotoUIPrincipal)
        self.btnRegresar.clicked.connect(self.eventBtnRegresar)        
        #self.btnContinuar.clicked.connect(self.gotoUIGraficas)
        self.btnContinuar.clicked.connect(self.eventBtnContinuar)
        self.actualizarBotones()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnContinuar.setText(_translate("MainWindow", "Continuar"))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar"))

    def actualizarBotones(self):
        self.btnContinuar.setText("Continuar")
        self.btnRegresar.setText("Regresar")

        if self.pantallaActual == self.PANT_INICIAL:
            self.btnRegresar.setVisible(False)
            self.btnContinuar.setVisible(False)
        elif self.pantallaActual == self.PANT_RESP_CONTROLADA:
            self.btnRegresar.setVisible(True)
            self.btnContinuar.setVisible(True)
        elif self.pantallaActual == self.PANT_RESP_ASISTIDA:
            self.btnRegresar.setVisible(True)
            self.btnContinuar.setVisible(True)
        elif self.pantallaActual == self.PANT_AJUSTES:
            self.btnRegresar.setVisible(True)
            self.btnContinuar.setVisible(True)
        elif self.pantallaActual == self.PANT_GRAFICAS:
            self.btnRegresar.setVisible(True)
            self.btnContinuar.setVisible(False)
        elif self.pantallaActual == self.PANT_MAXMINPARAMETROS:
            self.btnRegresar.setText("Regresar a Menu Principal")
            self.btnRegresar.setVisible(True)
            self.btnContinuar.setText("Guardar Parametros")
            self.btnContinuar.setVisible(True)
            
    def eventBtnRegresar(self):
        if self.pantallaActual == self.PANT_RESP_CONTROLADA:
            self.gotoUIPrincipal()
        elif self.pantallaActual == self.PANT_RESP_ASISTIDA:
            self.gotoUIPrincipal()
        elif self.pantallaActual == self.PANT_AJUSTES:
            self.gotoUIPrincipal()
        elif self.pantallaActual == self.PANT_GRAFICAS:
            if self.pantallaAnterior == self.PANT_RESP_CONTROLADA:
                self.gotoUIRespiracionControlada()
            elif self.pantallaAnterior == self.PANT_RESP_ASISTIDA:
                self.gotoUIRespiracionAsistida()
        elif self.pantallaActual == self.PANT_MAXMINPARAMETROS:
            self.gotoUIPrincipal()

    def eventBtnContinuar(self):
        if self.pantallaActual == self.PANT_RESP_CONTROLADA:
            self.pantallaAnterior = self.PANT_RESP_CONTROLADA
            self.gotoUIGraficas()
        elif self.pantallaActual == self.PANT_RESP_ASISTIDA:
            self.pantallaAnterior = self.PANT_RESP_ASISTIDA
            self.gotoUIGraficas()
        elif self.pantallaActual == self.PANT_AJUSTES:
            if self.uiAjustes.txtPassword.text() == self.uiAjustes.PASSWORD:
                self.gotoUIMaxMinParametros()
        elif self.pantallaActual == self.PANT_MAXMINPARAMETROS:
            f = open("./max_min_data.txt","w") #abrir archivo para lectura y escritura
            #se guardan los maximos y minimos en el arhivo data.txt
            f.write("%d\n%d\n" % (self.uiMaxMinParametros.spinFrecRespMax.value(), self.uiMaxMinParametros.spinFrecRespMin.value()) )
            f.write("%d\n%d\n" % (self.uiMaxMinParametros.spinVolTidalMax.value(), self.uiMaxMinParametros.spinVolTidalMin.value()) )
            f.write("%d\n%d\n" % (self.uiMaxMinParametros.spinRelIEMax.value(), self.uiMaxMinParametros.spinRelIEMin.value()) )
            f.write("%d\n%d\n" % (self.uiMaxMinParametros.spinSensMax.value(), self.uiMaxMinParametros.spinSensMin.value()) )
            f.write("%d\n%d" % (self.uiMaxMinParametros.spinOxiMax.value(), self.uiMaxMinParametros.spinOxiMin.value()) )
            f.close()

    def gotoUIPrincipal(self):
        self.verticalLayout.removeWidget(self.form2)
        self.form2.setParent(None)
        self.verticalLayout.removeWidget(self.form3)
        self.form3.setParent(None)
        self.verticalLayout.removeWidget(self.form4)
        self.form4.setParent(None)
        self.verticalLayout.removeWidget(self.form5)
        self.form5.setParent(None)
        self.verticalLayout.removeWidget(self.form6)
        self.form6.setParent(None)
        self.verticalLayout.addWidget(self.form)
        self.pantallaActual = self.PANT_INICIAL
        self.actualizarBotones()

    def gotoUIRespiracionControlada(self):        
        self.verticalLayout.removeWidget(self.form)
        self.form.setParent(None)
        self.verticalLayout.removeWidget(self.form3)
        self.form3.setParent(None)
        self.verticalLayout.removeWidget(self.form4)
        self.form4.setParent(None)
        self.verticalLayout.removeWidget(self.form5)
        self.form5.setParent(None)
        self.verticalLayout.removeWidget(self.form6)
        self.form6.setParent(None)
        self.uiRespiracionControlada.actualizarParametros()
        self.verticalLayout.addWidget(self.form2)
        self.pantallaActual = self.PANT_RESP_CONTROLADA
        self.actualizarBotones()	

    def gotoUIRespiracionAsistida(self):     
        self.verticalLayout.removeWidget(self.form)
        self.form.setParent(None)
        self.verticalLayout.removeWidget(self.form2)
        self.form2.setParent(None)        
        self.verticalLayout.removeWidget(self.form4)
        self.form4.setParent(None)
        self.verticalLayout.removeWidget(self.form5)
        self.form5.setParent(None)
        self.verticalLayout.removeWidget(self.form6)
        self.form6.setParent(None)
        self.uiRespiracionAsistida.actualizarParametros()
        self.verticalLayout.addWidget(self.form3)        
        self.pantallaActual = self.PANT_RESP_ASISTIDA
        self.actualizarBotones()	

    def gotoUIGraficas(self):
        self.verticalLayout.removeWidget(self.form)
        self.form.setParent(None)
        self.verticalLayout.removeWidget(self.form2)
        self.form2.setParent(None)
        self.verticalLayout.removeWidget(self.form3)
        self.form3.setParent(None)
        self.verticalLayout.removeWidget(self.form5)
        self.form5.setParent(None)
        self.verticalLayout.removeWidget(self.form6)
        self.form6.setParent(None)
        self.verticalLayout.addWidget(self.form4)
        self.pantallaActual = self.PANT_GRAFICAS
        self.actualizarBotones()

    def gotoUIAjustes(self):
        self.verticalLayout.removeWidget(self.form)
        self.form.setParent(None)
        self.verticalLayout.removeWidget(self.form2)
        self.form2.setParent(None)
        self.verticalLayout.removeWidget(self.form3)
        self.form3.setParent(None)        
        self.verticalLayout.removeWidget(self.form4)
        self.form4.setParent(None)
        self.verticalLayout.removeWidget(self.form6)
        self.form6.setParent(None)
        self.verticalLayout.addWidget(self.form5)
        self.pantallaActual = self.PANT_AJUSTES
        self.actualizarBotones()

    def gotoUIMaxMinParametros(self):
        self.verticalLayout.removeWidget(self.form)
        self.form.setParent(None)
        self.verticalLayout.removeWidget(self.form2)
        self.form2.setParent(None)
        self.verticalLayout.removeWidget(self.form3)
        self.form3.setParent(None)        
        self.verticalLayout.removeWidget(self.form4)
        self.form4.setParent(None)
        self.verticalLayout.removeWidget(self.form5)
        self.form5.setParent(None)
        self.verticalLayout.addWidget(self.form6)
        self.pantallaActual = self.PANT_MAXMINPARAMETROS
        self.actualizarBotones()	
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

