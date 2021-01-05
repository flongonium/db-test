import numpy as np
import pandas as pd
import sys

# plot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# window

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

# database and settings
import pymysql
import configparser
settings = configparser.ConfigParser()
settings.read("config/myApp.cfg")


class readTemperature(FigCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 80):
        fig = Figure(figsize =(width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        FigCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()
    
    def plot(self):
        pass
        # db call
        

        # Pre Processing
        

        # plot     


class readHumidity(FigCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 80):
        fig = Figure(figsize =(width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        FigCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()

    def plot(self):
        pass
        # db call
        

        # Pre Processing
        

        # plot          


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        title = "Sauna Stats"
        top = 50
        left = 50
        width = 750
        height = 450

        self.setToolTip("Sauna Stats Demo")
        self.setGeometry(top, left, width, height)
        self.setWindowTitle(title)

        self.MyUI()

    def MyUI(self):
        QToolTip.setFont(QFont('Arial', 11))

        # Exit Button
        buttonExit = QPushButton('Exit', self)
        buttonExit.move(640, 420)
        buttonExit.setToolTip('close application')
        buttonExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        # Load Data Button
        buttonTemperature = QPushButton('Temperature', self)
        buttonTemperature.move(20, 420)
        buttonTemperature.setToolTip('show temperature')
        buttonTemperature.clicked.connect(self.loadTemperature)

        # OEE Button
        buttonHumidity = QPushButton('Humidity', self)
        buttonHumidity.move(120, 420)
        buttonHumidity.setToolTip('show humidity')
        buttonHumidity.clicked.connect(self.loadHumidity)


    def loadTemperature(self):
        sc = readTemperature(self, width=8, height=4, dpi=100)
        sc.move(0, 0)
        sc.show()
    
    def loadHumidity(self):
        sc = readHumidity(self, width=8, height=4, dpi=100)
        sc.move(0, 0)
        sc.show()


def main():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())  

if __name__ == '__main__':
    main()