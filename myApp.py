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

# API - https://www.alphavantage.co/documentation/ - pip install alpha-vantage
from alpha_vantage.timeseries import TimeSeries as TiSe


class StockExchange(FigCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 80):
        fig = Figure(figsize =(width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        FigCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()
    
    def plot(self):
        # API call
        key = 'INSERT YOUR OWN KEY'
        ts = TiSe(key, output_format='pandas')
        sun, sunMeta =  ts.get_intraday(symbol='SUN', interval='1min')

        # Pre Processing
        topVal = sun.head(1)
        topVal.columns = sun.columns.str.replace(r"\d\.\s", "")
        print(sun)

        # plot     
        ax = self.figure.add_subplot(111)
        
        ax.set(title='Sulzer Börsenkurs SIX'
        , xlabel=f'{str(topVal.index[0])} CH Zeit'
        , ylabel='CHF'
        , ylim=(0, topVal['high'].max()+10))
        ax.bar("Eröffnung", topVal["open"], color="b", label="Eröffnung")
        ax.bar("Maximum", topVal["high"], color="g", label="Maximum")
        ax.bar("Minimum", topVal["low"], color="r", label="Minimum")

class OEE(FigCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 80):
        fig = Figure(figsize =(width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        FigCanvas.__init__(self, fig)
        self.setParent(parent)
        self.OEE()

    def OEE(self):
        ax = self.figure.add_subplot(111)

        ax.set(title='Sulzer OEE - Site 2/ODI'
        , xlabel=f'Attribut'
        , ylabel='Prozent'
        , ylim=(0, 100))
        labels = ['Wirtschaftlichkeit', 'Leistung', 'Qualität', 'OEE']

        x = np.random.uniform(low=0.85, high=0.99, size=3)
        ax.bar(labels[0], x[0]*100, color="g", label="open")
        ax.bar(labels[1], x[1]*100, color="b", label="high")
        ax.bar(labels[2], x[2]*100, color="m", label="low")
        ax.bar(labels[3], x[0]*x[1]*x[2]*100, color='r')
        ax.axhline(y=92, xmin=0, xmax=1, color='k')
        print(x)

class StockExchangeGraph(FigCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 80):
        fig = Figure(figsize =(width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        FigCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()
    
    def plot(self):
        # API call
        key = 'INSERT OWN KEY'
        ts = TiSe(key, output_format='pandas')
        sun, sunMeta =  ts.get_intraday(symbol='SUN', interval='1min', outputsize='full')

        # plot     
        ax = self.figure.add_subplot(111)
        ax.set(title = 'Intraday Time Series of the SUN stock (per day)'
        , xlabel = 'Time'
        , ylabel = 'US Dollar' 
        )
        ax.plot(sun['4. close'])
        print(sun.head(1))

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        title = "Sulzer Ltd - Live plot demo"
        top = 50
        left = 50
        width = 750
        height = 450

        self.setToolTip("Sulzer Stock Exchange")
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
        buttonLoad = QPushButton('Stock Data', self)
        buttonLoad.move(20, 420)
        buttonLoad.setToolTip('load Stock Exchange data and plot')
        buttonLoad.clicked.connect(self.loadPressed)

        # OEE Button
        buttonOEE = QPushButton('OEE Data', self)
        buttonOEE.move(120, 420)
        buttonOEE.setToolTip('load OEE data and plot')
        buttonOEE.clicked.connect(self.loadOEE)

        # OEE Button
        buttonStock = QPushButton('Stock Data TS', self)
        buttonStock.move(220, 420)
        buttonStock.setToolTip('load Stock data and plot')
        buttonStock.clicked.connect(self.loadStock)

    def loadPressed(self):
        sc = StockExchange(self, width=8, height=4, dpi=100)
        sc.move(0, 0)
        sc.show()
    
    def loadOEE(self):
        sc = OEE(self, width=8, height=4, dpi=100)
        sc.move(0, 0)
        sc.show()
    
    def loadStock(self):
        sc = StockExchangeGraph(self, width=8, height=4, dpi=100)
        sc.move(0, 0)
        sc.show()


def main():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())  

if __name__ == '__main__':
    main()