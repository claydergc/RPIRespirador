from ui.RPIRespiradorUI import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        #self.label.setText("Haz clic en el boton")
        self.pushButton.setText("Presioname")
        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        self.pushButton.setText("Acabas de hacer clic en el boton!")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
