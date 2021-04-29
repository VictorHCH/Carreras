import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        '''Prueba xD'''


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()