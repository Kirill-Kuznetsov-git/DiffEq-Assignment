from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox


class CheckBoxes(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.checkbox_euler = QCheckBox(self)
        self.checkbox_euler.setText("Euler Method")
        self.checkbox_euler.setChecked(True)

        self.checkbox_euler_improved = QCheckBox(self)
        self.checkbox_euler_improved.setText("Euler Improved Method")
        self.checkbox_euler_improved.setChecked(True)

        self.checkbox_runge = QCheckBox(self)
        self.checkbox_runge.setText("Runge-Kutta Method")
        self.checkbox_runge.setChecked(True)

        self.layout.addWidget(self.checkbox_euler)
        self.layout.addWidget(self.checkbox_euler_improved)
        self.layout.addWidget(self.checkbox_runge)
        self.setGeometry(820, 40, 200, 100)
