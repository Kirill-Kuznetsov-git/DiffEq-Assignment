from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QHBoxLayout, QVBoxLayout

from CustomCLasses.SpinBoxes import SpinBoxes
from CustomCLasses.CheckBoxes import CheckBoxes
from FirstWindow import FirstWindow
from SecondWindow import SecondWindow
from ThirdWindow import ThirdWindow

import sys


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 350
        self.top = 150
        self.width = 1000
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table = Table(self)
        self.table.setGeometry(0, 0, 800, 500)
        self.checkboxes = CheckBoxes(self)
        self.spinboxes = SpinBoxes(self)

        self.show()


class Table(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.table_widget = QTabWidget(self)
        self.table_widget.setGeometry(0, 0, 800, 500)

        self.tab1 = FirstWindow(self)
        self.table_widget.addTab(self.tab1, 'Tab1')
        self.tab2 = SecondWindow(self)
        self.table_widget.addTab(self.tab2, 'Tab2')
        self.tab3 = ThirdWindow(self)
        self.table_widget.addTab(self.tab3, 'Tab3')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
