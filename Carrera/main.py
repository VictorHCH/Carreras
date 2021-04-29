import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        text = QLabel("Bienvenido")
        self.setCentralWidget(text)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()