import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class WorkerSignals(QObject):
    data = pyqtSignal(tuple)


class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.switch = True

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background: rgb(242,242,242,250); color: black; border-top-right-radius: 0px;"
                           " border-top-right-radius : 0px;"
                           " border-bottom-left-radius : 6px;"
                           " border-bottom-right-radius : 6px;"
                           )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(900, 600)

        self.titulo = QLabel("Carrera")
        self.titulo.setFont(QFont("Segoe UI Light", 12))
        self.barra = QToolBar("barra de herramientas")
        self.barra.setIconSize(QSize(16, 16))
        self.addToolBar(self.barra)
        self.barra.setStyleSheet("background: rgb(165,165,165,250); color: white; border-top-right-radius: 8px;"
                                 "border-top-right-radius: 8px;"
                                 "border-bottom-left-radius: 0px;"
                                 "border-bottom-right-radius: 0px")

 #---------------------------------Barra de tareas----------------------------------#
        izquierda = QWidget()
        izquierda.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        derecha = QWidget()
        derecha.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        boton_accion = QAction(QIcon("Imagenes\Cerrar.png"), "Cerrar", self)
        boton_accion.triggered.connect(self.cerrar)
        self.barra.addAction(boton_accion)

        boton_accion2 = QAction(QIcon("Imagenes\Minimizar.png"), "Minimizar", self)
        boton_accion2.triggered.connect(self.minimizar)
        self.barra.addAction(boton_accion2)
        self.barra.setMovable(False)
        self.barra.addWidget(izquierda)
        self.barra.addWidget(self.titulo)
        self.barra.addWidget(derecha)


#------------------------------------------Fondo---------------------------------------------------#
        pixmap = QPixmap("Imagenes\Banqueta.png")
        bg = QLabel(self)
        pixmap = pixmap.scaled(1200, 1200, Qt.KeepAspectRatio, Qt.FastTransformation)
        bg.setPixmap(pixmap)

        lo = QHBoxLayout()
        lo.addWidget(bg)
        widget = QWidget()
        widget.setLayout(lo)
        self.setCentralWidget(widget)
# ------------------------------------------Boton------------------------------------------------#
   # Esta parte aun no la arreglo, el icono del boton no se asigna bien y no se hace transparente xD
    
        Prueba = QPushButton(self)
        botn = QPixmap("Imagenes\Boton.png")
        ico = QIcon(botn)
        Prueba.setIcon(ico)
        Prueba.setAttribute(Qt.WA_TranslucentBackground, True)
        Prueba.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        Prueba.setIconSize(pixmap.rect().size())
        Prueba.resize(212, 200)
        Prueba.setStyleSheet("border-radius: 5px; color: white; background: rgb(165,165,165); border: 2px solid white;")
        Prueba.move(int(1060 / 2 - 150 / 2), int(820 / 2 - 40 / 2))
        Prueba.clicked.connect(self.inicio_lcd)

# ------------------------------------------Titulo------------------------------------------------#
        pixmap = QPixmap("Imagenes\Carrera.png")
        titulo = QLabel(self)
        pixmap = pixmap.scaled(1000, 1000, Qt.KeepAspectRatio, Qt.FastTransformation)
        titulo.setAttribute(Qt.WA_TranslucentBackground, True)
        titulo.setPixmap(pixmap)
        titulo.resize(1000, 130)
        titulo.move(120, 150)

# ------------------------------------------Cronometro------------------------------------------------#
        self.lcd = QLCDNumber(self)
        self.lcd.setAttribute(Qt.WA_TranslucentBackground, True)
        self.lcd.display("00:00")
        self.lcd.resize(200, 100)
        self.lcd.move(975, 50)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.iniciar_timer)
        self.timer.setInterval(1000)
        self.time = 0

    def iniciar_timer(self):
        self.time += 1
        m = self.time / 60
        s = self.time % 60
        hora = str("%002d:%002d" %(m, s))
        self.lcd.display(hora)
        if self.time > 100:
            self.timer.stop()

    def inicio_lcd(self):
        QMessageBox.information(self, "Carrera", "La carrera a iniciado", QMessageBox.Ok)
        self.time = 0
        self.timer.start()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def minimizar(self):
        self.showMinimized()

    def cerrar(self):
        self.close()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()