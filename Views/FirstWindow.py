from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QHBoxLayout
from CustomCLasses.Canvas import MplCanvas


class FirstWindow(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.equations = parent.equations
        self.parent = parent

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
        leg = []
        for equation in self.equations:
            if equation.vision is True:
                leg.append(str(type(equation)).split("Model.")[1].split("'")[0])
                res = equation.get_equation()
                self.canvas.axes.plot(res[0], res[1], color=self.colors[str(type(equation)).split("Model.")[1].split("'")[0]])
        self.canvas.axes.legend(leg)
        self.canvas.draw()


