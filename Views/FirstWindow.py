from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pylab as plt

import numpy as np

from Model import *


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class FirstWindow(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.equations = []
        self.parent = parent

        self.equations.append(AnalyticalSolution(2, 0, 100, 120))
        self.equations.append(EulerMethod(2, 0, 100, 120))
        self.equations.append(ImprovedEulerMethod(2, 0, 100, 120))
        self.equations.append(RungeMethod(2, 0, 100, 120))

        self._main = QWidget(self)
        self._main.setGeometry(-10, 0, 800, 500)
        layout = QHBoxLayout(self._main)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        self.colors = {"AnalyticalSolution": 'black', "EulerMethod": 'red', "ImprovedEulerMethod": 'blue',
                       'RungeMethod': 'green'}

        self.update()

    def change_attributes(self, attributes: dict):
        for i in range(len(self.equations)):
            if attributes.get('x0'): self.equations[i].set_x0(attributes['x0'])
            if attributes.get('y0'): self.equations[i].set_y0(attributes['y0'])
            if attributes.get('N'): self.equations[i].set_N(attributes['N'])
            if attributes.get('X'): self.equations[i].set_X(attributes['X'])
        self.update()

    def change_checkboxes(self, name: str, value: bool):
        for i in range(len(self.equations)):
            if str(type(self.equations[i])).split("Model.")[1].split("'")[0] == name:
                self.equations[i].vision = value
        self.update()

    def update(self):
        self.canvas.axes.cla()
        for equation in self.equations:
            if equation.vision is True:
                res = equation.get_equation()
                self.canvas.axes.plot(res[0], res[1], color=self.colors[str(type(equation)).split("Model.")[1].split("'")[0]])
        self.canvas.draw()


