# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIRespiracionAsistida.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RespiracionAsistida(object):
    def setupUi(self, RespiracionAsistida):
        RespiracionAsistida.setObjectName("RespiracionAsistida")
        RespiracionAsistida.resize(800, 480)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(RespiracionAsistida)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, 50, 5, 50)
        self.gridLayout_2.setVerticalSpacing(50)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(5, 50, 5, 50)
        self.gridLayout_4.setVerticalSpacing(50)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")

        #self.sldVolumenTidal = QtWidgets.QSlider(RespiracionAsistida)
        #self.sldVolumenTidal.setOrientation(QtCore.Qt.Vertical)
        #self.sldVolumenTidal.setObjectName("sldVolumenTidal")
        #self.gridLayout_7.addWidget(self.sldVolumenTidal, 1, 0, 1, 1)
        self.sldVolumenTidal = QtWidgets.QSlider(RespiracionAsistida)
        self.sldVolumenTidal.setOrientation(QtCore.Qt.Vertical)
        self.sldVolumenTidal.setObjectName("sldVolumenTidal")
        self.sldVolumenTidal.setMinimum(200)
        self.sldVolumenTidal.setMaximum(800)
        self.sldVolumenTidal.setValue(200)        
        self.sldVolumenTidal.setTickInterval(5)
        self.sldVolumenTidal.valueChanged.connect(self.sldVolumenTidalValueChanged)
        self.gridLayout_7.addWidget(self.sldVolumenTidal, 1, 0, 1, 1)
        
        self.label_7 = QtWidgets.QLabel(RespiracionAsistida)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(RespiracionAsistida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(RespiracionAsistida)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.lblVolumenTidal = QtWidgets.QLabel(RespiracionAsistida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVolumenTidal.sizePolicy().hasHeightForWidth())
        self.lblVolumenTidal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblVolumenTidal.setFont(font)
        self.lblVolumenTidal.setObjectName("lblVolumenTidal")
        self.gridLayout_4.addWidget(self.lblVolumenTidal, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(5, 50, 5, 50)
        self.gridLayout_8.setVerticalSpacing(50)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_4.addLayout(self.gridLayout_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setContentsMargins(5, 50, 5, 50)
        self.gridLayout_10.setVerticalSpacing(50)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_5.addLayout(self.gridLayout_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setContentsMargins(5, 50, 5, 50)
        self.gridLayout_12.setVerticalSpacing(50)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout.addLayout(self.gridLayout_12)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RespiracionAsistida)
        QtCore.QMetaObject.connectSlotsByName(RespiracionAsistida)

        f = open("./max_min_data.txt","r") #abrir archivo para lectura y escritura
        lines = f.readlines()

        if len(lines)==10:
            self.sldVolumenTidal.setMaximum(int(lines[2]))
            self.sldVolumenTidal.setMinimum(int(lines[3]))
            self.label_6.setText(lines[2].strip() + " ml")
            self.label_8.setText(lines[3].strip() + " ml")
            self.sldVolumenTidal.setValue(int(lines[3]))

    def actualizarParametros(self):
        f = open("./max_min_data.txt","r") #abrir archivo para lectura y escritura
        lines = f.readlines()

        if len(lines)==10:
            self.sldVolumenTidal.setMaximum(int(lines[2]))
            self.sldVolumenTidal.setMinimum(int(lines[3]))
            self.label_6.setText(lines[2].strip() + " ml")
            self.label_8.setText(lines[3].strip() + " ml")
            self.sldVolumenTidal.setValue(int(lines[3]))


    def retranslateUi(self, RespiracionAsistida):
        _translate = QtCore.QCoreApplication.translate
        RespiracionAsistida.setWindowTitle(_translate("RespiracionAsistida", "Form"))
        self.label_6.setText(_translate("RespiracionAsistida", "800 ml"))
        self.label_8.setText(_translate("RespiracionAsistida", "200 ml"))
        self.lblVolumenTidal.setText(_translate("RespiracionAsistida", "Vol. Tidal:   "))

    def sldVolumenTidalValueChanged(self):
    	self.lblVolumenTidal.setText( "Vol. Tidal: " + str(self.sldVolumenTidal.value()) )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RespiracionAsistida = QtWidgets.QWidget()
    ui = Ui_RespiracionAsistida()
    ui.setupUi(RespiracionAsistida)
    RespiracionAsistida.show()
    sys.exit(app.exec_())

