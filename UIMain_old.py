from PyQt5 import QtCore, QtGui, QtWidgets
from ui.UIPrincipal import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
	#objeto de clase Ui_Form	
	self.Form = QtWidgets.QWidget()
    	self.ui = Ui_Form()
    	self.ui.setupUi(self.Form)
	self.horizontalLayout.addWidget(self.Form)
	#objeto de clase Ui_Form

	MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	MainWindow.setWindowState(QtCore.Qt.WindowMaximized)
	MainWindow.showFullScreen()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Respirador Electroneumatico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

