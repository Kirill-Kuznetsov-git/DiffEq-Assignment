from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np


class FirstWindow(QWidget):
    def __init__(self, parent, equations):
        super(QWidget, self).__init__(parent)
        self.equations = equations

        self._main = QWidget(self)
        self._main.setGeometry(-10, 0, 800, 500)
        layout = QHBoxLayout(self._main)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)
        self.canvas = self.canvas.figure.subplots()

        self.colors = {"AnalyticalSolution": 'black', "EulerMethod": 'red', "ImprovedEulerMethod": 'blue',
                       'RungeMethod': 'green'}
        for equation in self.equations:
            res = equation.get_equation()
            self.canvas.plot(res[0], res[1], color=self.colors[str(type(equation)).split("Model.")[1].split("'")[0]])



