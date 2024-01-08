from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)

class Button(QPushButton):
    def __init__(self, text) -> None:
        super().__init__(text)
        self.setFixedSize(100, 50)
        self.setStyleSheet('font-size: 24px')

class Button1(QPushButton):
    def __init__(self, text) -> None:
        super().__init__(text)
        self.setFixedHeight(50)
        self.setStyleSheet('font-size:24px;')

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 300)
        self.setWindowTitle("Calculator")
        font = self.font()

        self.v_box = QVBoxLayout()
        self.h_box0 = QHBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.input = QLineEdit(self)
        self.input.setFixedHeight(50)
        self.h_box0.addWidget(self.input)

        self.btn1 = Button('1')
        self.btn2 = Button('2')
        self.btn3 = Button('3')
        self.btn_devide = Button('/')

        self.btn4 = Button('4')
        self.btn5 = Button('5')
        self.btn6 = Button('6')
        self.btn_multiplication = Button('*')

        self.btn7 = Button('7')
        self.btn8 = Button('8')
        self.btn9 = Button('9')
        self.btn_subtraction = Button('-')

        self.btn0 = Button1('0')
        self.btn0.setFixedHeight(50)
        self.btn_equal = Button1('=')
        self.btn_equal.setFixedHeight(50)
        self.btn_addition = Button1('+')
        self.btn_addition.setFixedHeight(50)

        self.h_box1.addWidget(self.btn1)
        self.h_box1.addWidget(self.btn2)
        self.h_box1.addWidget(self.btn3)
        self.h_box1.addWidget(self.btn_devide)

        self.h_box2.addWidget(self.btn4)
        self.h_box2.addWidget(self.btn5)
        self.h_box2.addWidget(self.btn6)
        self.h_box2.addWidget(self.btn_multiplication)

        self.h_box3.addWidget(self.btn7)
        self.h_box3.addWidget(self.btn8)
        self.h_box3.addWidget(self.btn9)
        self.h_box3.addWidget(self.btn_subtraction)

        self.h_box4.addWidget(self.btn0)
        self.h_box4.addWidget(self.btn_equal)
        self.h_box4.addWidget(self.btn_addition)

        self.v_box.addLayout(self.h_box0)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)

        self.show()


app = QApplication([])
win = Window()
app.exec_()