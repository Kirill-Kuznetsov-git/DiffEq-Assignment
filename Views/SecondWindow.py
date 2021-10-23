from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout
from CustomCLasses.Canvas import MplCanvas


from Model import *


class SecondWindow(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        self.equations = parent.equations

        self._main = QWidget(self)
        self._main.setGeometry(-10, 0, 800, 500)
        layout = QHBoxLayout(self._main)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        self.colors = {"AnalyticalSolution": 'black', "EulerMethod": 'red', "ImprovedEulerMethod": 'blue',
                       'RungeMethod': 'green'}

        self.update()

    def update(self):
        self.canvas.axes.cla()
        for i in range(1, len(self.equations)):
            if self.equations[i].vision is True:
                print(self.equations[i])
                res = self.equations[i].get_lte(self.equations[0])
                self.canvas.axes.plot(res[0], res[1], color=self.colors[str(type(self.equations[i])).split("Model.")[1].split("'")[0]])
        self.canvas.draw()
