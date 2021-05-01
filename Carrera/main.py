import sys
import time
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, QTimer, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QLCDNumber


class WorkerSignal(QObject):
    """ Define las señales disponibles desde la ejecucion de la Tarea  (hilo)"""

    progress = pyqtSignal(int)


class Worker(QRunnable):
    """Worker Thread

        Inherits from QRunnable to """

    def __init__(self):
        super().__init__()
        self.signals = WorkerSignal()

    @pyqtSlot()
    def run(self):
        total = 1000
        for n in range(total):
            progress = int(100 * float(n + 1) / total)
            self.signals.progress.emit(progress)
            time.sleep(0.1)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        gestor = QVBoxLayout()
        self.progreso = QLCDNumber()
        widget = QWidget()
        btnIniciar = QPushButton("Iniciar")
        btnIniciar.clicked.connect(self.ejecutar)

        gestor.addWidget(self.progreso)
        gestor.addWidget(btnIniciar)
        widget.setLayout(gestor)
        self.setCentralWidget(widget)
        self.threadpool = QThreadPool()
        print("Multihilos con un maximo %d hilos" % self.threadpool.maxThreadCount())

    def ejecutar(self):
        worker = Worker()
        worker.signals.progress.connect(self.actualizarProgreso)
        self.threadpool.start(worker)

    def actualizarProgreso(self, progress):
        self.progreso.display(progress)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()