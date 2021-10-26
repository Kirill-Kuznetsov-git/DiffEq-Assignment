from PyQt5.QtWidgets import QWidget, QVBoxLayout,\
    QSpinBox, QLabel, QHBoxLayout


class SpinBoxes(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.parent = parent

        self.widget_1 = QWidget()
        self.widget_1.layout = QHBoxLayout(self)
        self.x0 = QSpinBox(self)
        self.x0.setValue(2)
        self.x0.setMaximum(100000)
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
        self.label_y0 = QLabel(self)
        self.label_y0.setText("y_0:")
        self.widget_2.layout.addWidget(self.label_y0)
        self.widget_2.layout.addWidget(self.y0)
        self.widget_2.setLayout(self.widget_2.layout)

        self.widget_3 = QWidget()
        self.widget_3.layout = QHBoxLayout(self)
        self.X = QSpinBox(self)
        self.X.setMaximum(100000)
        self.X.setValue(12)
        self.label_X = QLabel(self)
        self.label_X.setText("X:  ")
        self.widget_3.layout.addWidget(self.label_X)
        self.widget_3.layout.addWidget(self.X)
        self.widget_3.setLayout(self.widget_3.layout)

        self.widget_5 = QWidget()
        self.widget_5.layout = QHBoxLayout(self)
        self.n0 = QSpinBox(self)
        self.n0.setMaximum(100000)
        self.n0.setValue(10)
        self.label_n0 = QLabel(self)
        self.label_n0.setText("n_0:  ")
        self.widget_5.layout.addWidget(self.label_n0)
        self.widget_5.layout.addWidget(self.n0)
        self.widget_5.setLayout(self.widget_5.layout)

        self.widget_4 = QWidget()
        self.widget_4.layout = QHBoxLayout(self)
        self.N = QSpinBox(self)
        self.N.setMaximum(100000)
        self.N.setValue(120)
        self.label_N = QLabel(self)
        self.label_N.setText("N:  ")
        self.widget_4.layout.addWidget(self.label_N)
        self.widget_4.layout.addWidget(self.N)
        self.widget_4.setLayout(self.widget_4.layout)

        self.label_error = QLabel(self)
        self.label_error.setText("")

        self.layout.addWidget(self.widget_1)
        self.layout.addWidget(self.widget_2)
        self.layout.addWidget(self.widget_3)
        self.layout.addWidget(self.widget_4)
        self.layout.addWidget(self.widget_5)
        self.layout.addWidget(self.label_error)
        self.setGeometry(790, 150, 200, 270)

        self.connect_all()

    def connect_all(self):
        self.x0.valueChanged.connect(self.change_value)
        self.y0.valueChanged.connect(self.change_value)
        self.n0.valueChanged.connect(self.change_value)
        self.N.valueChanged.connect(self.change_value)
        self.X.valueChanged.connect(self.change_value)

    def change_value(self):
        ans = self.parent.change_spinboxes({"x0": self.x0.value(), "y0": self.y0.value(), "X": self.X.value(),
                                      "n0": self.n0.value(), "N": self.N.value()})
        if ans["Error"] == 1:
            self.label_error.setText(ans['Description'])
        elif ans["Error"] == 0:
            self.label_error.setText("")
