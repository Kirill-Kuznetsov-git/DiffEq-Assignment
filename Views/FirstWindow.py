from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np

from Model import *


class FirstWindow(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.equations = []
        self.equations.append(AnalyticalSolution(2, 0, 100, 200))
        self.equations.append(EulerMethod(2, 0, 100, 200))
        self.equations.append(ImprovedEulerMethod(2, 0, 100, 200))
        self.equations.append(RungeMethod(2, 0, 100, 200))

        self._main = QWidget(self)
        self._main.setGeometry(-10, 0, 800, 500)
        layout = QHBoxLayout(self._main)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)
        self._canvas = self.canvas.figure.subplots()

        self.colors = {"AnalyticalSolution": 'black', "EulerMethod": 'red', "ImprovedEulerMethod": 'blue',
                       'RungeMethod': 'green'}

        self.draw()

    def draw(self):
        for equation in self.equations:
            res = equation.get_equation()
            self._canvas.plot(res[0], res[1], color=self.colors[str(type(equation)).split("Model.")[1].split("'")[0]])



