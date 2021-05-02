import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel


<<<<<<< HEAD
class WorkerSignal(QObject):
    """ Define las señales disponibles desde la ejecucion de la Tarea  (hilo)"""

    progress = pyqtSignal(int)


class Worker(QRunnable):
=======
class MainWindow(QMainWindow):
>>>>>>> parent of e35213c (Version beta 1.0)
    def __init__(self):
        super().__init__()
        text = QLabel("Bienvenido")
        self.setCentralWidget(text)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()