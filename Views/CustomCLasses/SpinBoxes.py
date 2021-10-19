from PyQt5.QtWidgets import QWidget, QVBoxLayout,\
    QSpinBox, QLabel, QHBoxLayout


class SpinBoxes(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.widget_1 = QWidget()
        self.widget_1.layout = QHBoxLayout(self)
        self.x0 = QSpinBox(self)
        self.x0.setValue(2)
        self.x0.setMaximum(100000)
        self.x0.valueChanged.connect(self.change_x0)
        self.label_x0 = QLabel(self)
        self.label_x0.setText("x_0:")
        self.widget_1.layout.addWidget(self.label_x0)
        self.widget_1.layout.addWidget(self.x0)
        self.widget_1.setLayout(self.widget_1.layout)

        self.widget_2 = QWidget()
        self.widget_2.layout = QHBoxLayout(self)
        self.y0 = QSpinBox(self)
        self.y0.setValue(0)
        self.y0.setMaximum(100000)
        self.y0.valueChanged.connect(self.change_y0)
        self.label_y0 = QLabel(self)
        self.label_y0.setText("y_0:")
        self.widget_2.layout.addWidget(self.label_y0)
        self.widget_2.layout.addWidget(self.y0)
        self.widget_2.setLayout(self.widget_2.layout)

        self.widget_3 = QWidget()
        self.widget_3.layout = QHBoxLayout(self)
        self.X = QSpinBox(self)
        self.X.setMaximum(100000)
        self.X.valueChanged.connect(self.change_X)
        self.X.setValue(100)
        self.label_X = QLabel(self)
        self.label_X.setText("X:  ")
        self.widget_3.layout.addWidget(self.label_X)
        self.widget_3.layout.addWidget(self.X)
        self.widget_3.setLayout(self.widget_3.layout)

        self.widget_5 = QWidget()
        self.widget_5.layout = QHBoxLayout(self)
        self.n0 = QSpinBox(self)
        self.n0.setValue(10)
        self.n0.setMaximum(100000)
        self.n0.valueChanged.connect(self.change_n0)
        self.label_n0 = QLabel(self)
        self.label_n0.setText("n_0:  ")
        self.widget_5.layout.addWidget(self.label_n0)
        self.widget_5.layout.addWidget(self.n0)
        self.widget_5.setLayout(self.widget_5.layout)

        self.widget_4 = QWidget()
        self.widget_4.layout = QHBoxLayout(self)
        self.N = QSpinBox(self)
        self.N.setValue(40)
        self.N.setMaximum(100000)
        self.N.valueChanged.connect(self.change_N)
        self.label_N = QLabel(self)
        self.label_N.setText("N:  ")
        self.widget_4.layout.addWidget(self.label_N)
        self.widget_4.layout.addWidget(self.N)
        self.widget_4.setLayout(self.widget_4.layout)

        self.layout.addWidget(self.widget_1)
        self.layout.addWidget(self.widget_2)
        self.layout.addWidget(self.widget_3)
        self.layout.addWidget(self.widget_4)
        self.layout.addWidget(self.widget_5)
        self.setGeometry(790, 150, 200, 270)

    def change_x0(self):
        return self.x0.value()

    def change_y0(self):
        return self.y0.value()

    def change_X(self):
        return self.X.value()

    def change_N(self):
        return self.N.value()

    def change_n0(self):
        return self.n0.value()
