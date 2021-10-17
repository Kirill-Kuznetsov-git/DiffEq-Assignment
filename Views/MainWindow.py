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
        self.table.setGeometry(0, 0, 750, 500)
        self.checkboxes = CheckBoxes(self)
        self.spinboxes = SpinBoxes(self)
        self.list = QListWidget(self)
        self.list.setObjectName("listWidget")
        self.list.setGeometry(1070, 30, 200, 400)
        self.list.addItem("1/x+2*y/(x*ln(x))")

        self.show()


class Table(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.equations = []
        self.equations_cache = []

        self.table_widget = QTabWidget(self)
        self.table_widget.setGeometry(0, 0, 750, 500)

        self.equations.append(AnalyticalSolution(2, 0, 1000, 50))
        self.equations.append(EulerMethod(2, 0, 1000, 50))
        self.equations.append(ImprovedEulerMethod(2, 0, 1000, 50))
        self.equations.append(RungeMethod(2, 0, 1000, 50))

        self.tab1 = FirstWindow(self, self.equations)
        self.table_widget.addTab(self.tab1, 'Solutions')
        self.tab2 = SecondWindow(self)
        self.table_widget.addTab(self.tab2, 'LTE')
        self.tab3 = ThirdWindow(self)
        self.table_widget.addTab(self.tab3, 'GTE')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
