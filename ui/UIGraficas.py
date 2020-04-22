# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIGraficas.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.animation as animation
#import matplotlib.pyplot as plt

import sys
sys.path.append('../')

#from sensores.ecg import ECG
#from sensores.caudalimetro import Caudalimetro

class Ui_Graficas(object):
    def setupUi(self, Graficas):
        Graficas.setObjectName("Graficas")
        Graficas.resize(800, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Graficas)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(Graficas)
        self.widget_2.setObjectName("widget_2")
	
	# a figure instance to plot on
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.gridLayout.addWidget(self.canvas1, 0, 0, 1, 1)
	#self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.widget = QtWidgets.QWidget(Graficas)
        self.widget.setObjectName("widget")
        
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.gridLayout.addWidget(self.canvas2, 1, 0, 1, 1)
        #self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Graficas)
        QtCore.QMetaObject.connectSlotsByName(Graficas)
        
        # Parameters from first plot
        self.x_len1 = 800         # Number of points to display
        self.y_range1 = [0, 4]  # Range of possible Y values to display        
        self.xs1 = list(range(0, self.x_len1))
        self.ys1 = [0] * self.x_len1
        
        self.ax1 = self.figure1.add_subplot(1, 1, 1)	
        self.ax1.set_ylim(self.y_range1)
        self.line1, = self.ax1.plot(self.xs1, self.ys1)

        #self.ax.set_xlabel('Muestras')
        self.ax1.set_title('ECG')
        self.ax1.set_ylabel('Voltaje')

        # Initialize communication with TMP102
	#ecg = ECG()
        self.plotECG()

        # Parameters from second plot
        self.x_len2 = 800         # Number of points to display
        self.y_range2 = [0, 4]  # Range of possible Y values to display        
        self.xs2 = list(range(0, self.x_len2))
        self.ys2 = [0] * self.x_len2
        
        self.ax2 = self.figure2.add_subplot(1, 1, 1)	
        self.ax2.set_ylim(self.y_range2)
        self.line2, = self.ax2.plot(self.xs2, self.ys2)

        #self.ax.set_xlabel('Muestras')
        self.ax2.set_title('Caudal')
        self.ax2.set_ylabel('Voltaje')

        # Initialize communication with TMP102
	#ecg = ECG()
        self.plotCaudal()
        

    def retranslateUi(self, Graficas):
        _translate = QtCore.QCoreApplication.translate
        Graficas.setWindowTitle(_translate("Graficas", "Form"))

    def plotECG(self):
	
	# Create a blank line. We will update the line in animate
	#line, = ax.plot(xs, ys)

        # Set up plot to call animate() function periodically
        #ani = animation.FuncAnimation(self.figure1,
        self.ani1 = animation.FuncAnimation(self.figure1,
	    self.animate1,
	    fargs=(self.ys1,),
	    interval=50,
	    blit=True)        

    def animate1(self, i, ys):

        # Read temperature (Celsius) from TMP102
        #voltajeECG = round(ecg.getVoltage(), 5)
 
        # Add y to list
        #ys.append(voltajeECG)

        # Add y to list
        self.ys1.append(3)

        # Limit y list to set number of items
        self.ys1 = self.ys1[-self.x_len1:]

        # Update line with new Y values
        self.line1.set_ydata(self.ys1)

        return self.line1,

    def plotCaudal(self):
	
	# Create a blank line. We will update the line in animate
	#line, = ax.plot(xs, ys)

        # Set up plot to call animate() function periodically
        #ani = animation.FuncAnimation(self.figure1,
        self.ani2 = animation.FuncAnimation(self.figure2,
	    self.animate2,
	    fargs=(self.ys2,),
	    interval=50,
	    blit=True)

    def animate2(self, i, ys):

        # Read temperature (Celsius) from TMP102
        #voltajeECG = round(ecg.getVoltage(), 5)
 
        # Add y to list
        #ys.append(voltajeECG)

        # Add y to list
        self.ys2.append(2)

        # Limit y list to set number of items
        self.ys2 = self.ys2[-self.x_len2:]

        # Update line with new Y values
        self.line2.set_ydata(self.ys2)

        return self.line2,


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Graficas = QtWidgets.QWidget()
    ui = Ui_Graficas()
    ui.setupUi(Graficas)
    Graficas.show()
    sys.exit(app.exec_())    

