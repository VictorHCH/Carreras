import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        text = QLabel("Bienvenido")
        text2 = QLabel("Esta es una alfa!")
        lo = QHBoxLayout()
        lo.addWidget(text)
        lo.addWidget(text2)
        widget = QWidget()
        widget.setLayout(lo)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()