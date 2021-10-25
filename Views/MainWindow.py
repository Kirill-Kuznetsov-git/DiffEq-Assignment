from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QListWidget
from CustomCLasses.SpinBoxes import SpinBoxes
from CustomCLasses.CheckBoxes import CheckBoxes
from FirstWindow import FirstWindow
from SecondWindow import SecondWindow
from ThirdWindow import ThirdWindow

import sys

from Model import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Differential Equations'
        self.left = 350
        self.top = 150
        self.width = 1300
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table = Table(self)
        self.table.setGeometry(0, 0, 1030, 500)

        self.list = QListWidget(self)
        self.list.setObjectName("listWidget")
        self.list.setGeometry(1070, 30, 200, 400)
        self.list.addItem("1/x+2*y/(x*ln(x))")

        self.show()


class Table(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.parent = parent

        self.equations = []
        self.equations.append(AnalyticalSolution(2, 0, 12, 120))
        self.equations.append(EulerMethod(2, 0, 12, 120, 10))
        self.equations.append(ImprovedEulerMethod(2, 0, 12, 120, 10))
        self.equations.append(RungeMethod(2, 0, 12, 120, 10))

        self.table_widget = QTabWidget(self)
        self.table_widget.setGeometry(0, 0, 750, 500)

        self.checkboxes = CheckBoxes(self)
        self.spinboxes = SpinBoxes(self)

        self.tab1 = FirstWindow(self)
        self.table_widget.addTab(self.tab1, 'Solutions')
        self.tab2 = SecondWindow(self)
        self.table_widget.addTab(self.tab2, 'LTE')
        self.tab3 = ThirdWindow(self)
        self.table_widget.addTab(self.tab3, 'GTE')

    def change_spinboxes(self, attributes):
        for i in range(len(self.equations)):
            if attributes.get('x0'): self.equations[i].set_x0(attributes['x0'])
            if attributes.get('y0'): self.equations[i].set_y0(attributes['y0'])
            if attributes.get('n0') and str(type(self.equations[i])) != "<class 'Model.AnalyticalSolution'>": self.equations[i].set_n0(attributes['n0'])
            if attributes.get('N'): self.equations[i].set_N(attributes['N'])
            if attributes.get('X'): self.equations[i].set_X(attributes['X'])
        self.update_all()

    def change_checkboxes(self, name: str, value: bool):
        for i in range(len(self.equations)):
            if str(type(self.equations[i])).split("Model.")[1].split("'")[0] == name:
                self.equations[i].vision = value
        self.update_all()

    def update_all(self):
        self.tab1.update()
        self.tab2.update()
        self.tab3.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
