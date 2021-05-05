import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class WorkerSignals(QObject):
    data = pyqtSignal(int, int)


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
    
        self.Comenzar = QPushButton("Comenzar! ",self)
        self.Comenzar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Comenzar.setStyleSheet("border-radius: 5px; color: Blue; background:cyan; border: 2px solid white;")
        self.Comenzar.resize(190, 100)
        self.Comenzar.move(int(1250 / 2 - 190 / 2), int(820 / 2 - 40 / 2))
        self.Comenzar.clicked.connect(self.iniciarCarrera)
        #self.Comenzar.clicked.connect(self.ganador) (Evento para probar la ventana)

# ------------------------------------------Titulo------------------------------------------------#

        pixmap = QPixmap("Imagenes\Carrera.png")
        self.titulo = QLabel(self)
        pixmap = pixmap.scaled(1000, 1000, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.titulo.setAttribute(Qt.WA_TranslucentBackground, True)
        self.titulo.setPixmap(pixmap)
        self.titulo.resize(1000, 130)
        self.titulo.move(120, 150)

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
        self.lcd.hide()

# ------------------------------------------Liebre------------------------------------------------#
        mapLiebre = QPixmap("Imagenes\Liebre.png")
        self.liebre = QLabel(self)
        mapLiebre = mapLiebre.scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.liebre.setAttribute(Qt.WA_TranslucentBackground, True)
        self.liebre.setPixmap(mapLiebre)
        self.liebre.resize(200, 180)
        self.liebre.move(5, 180)
        self.liebre.hide()

# ------------------------------------------Tortuga------------------------------------------------#
        mapTortuga = QPixmap("Imagenes\Tortuga.png")
        self.tortuga = QLabel(self)
        mapTortuga = mapTortuga.scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.tortuga.setAttribute(Qt.WA_TranslucentBackground, True)
        self.tortuga.setPixmap(mapTortuga)
        self.tortuga.resize(200, 200)
        self.tortuga.move(5, 310)
        self.tortuga.hide()

    def iniciarCarrera(self):
        self.inicio_lcd()
        self.titulo.hide()
        self.liebre.show()
        self.tortuga.show()
        self.lcd.show()
        self.Comenzar.hide()
        self.Comenzar.setEnabled(False)

    def iniciar_timer(self):
        self.time += 1
        m = self.time / 60
        s = self.time % 60
        hora = str("%002d:%002d" %(m, s))
        self.lcd.display(hora)
        if self.time > 100:
            self.timer.stop()

    def inicio_lcd(self):
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

    def ganador(self):
        self.pod = podio()
        self.pod.show()

class podio(QMainWindow):
    def __init__(self):
        super().__init__()

#----------------------------------------------------Ventana-----------------------------------------------#
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("background: rgb(242,242,242,250); color: black; border-top-right-radius: 0px;"
                           " border-top-right-radius : 0px;"
                           " border-bottom-left-radius : 6px;"
                           " border-bottom-right-radius : 6px;"
                           )
# ------------------------------------Barra de tareas---------------------------------------#
        self.titulo = QLabel("Ganador")
        self.titulo.setFont(QFont("Segoe UI Light", 12))
        self.barra2 = QToolBar("barra de herramientas")
        self.barra2.setIconSize(QSize(16, 16))
        self.addToolBar(self.barra2)
        self.barra2.setStyleSheet("background: rgb(165,165,165,250); color: white; border-top-right-radius: 8px;"
                                 "border-top-right-radius: 8px;"
                                 "border-bottom-left-radius: 0px;"
                                 "border-bottom-right-radius: 0px")
        izquierda = QWidget()
        izquierda.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        derecha = QWidget()
        derecha.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        boton_accion = QAction(QIcon("Imagenes\Cerrar.png"), "Cerrar", self)
        boton_accion.triggered.connect(self.cerrar)
        self.barra2.addAction(boton_accion)
# ---------------------------------Barra de tareas----------------------------------#
        boton_accion2 = QAction(QIcon("Imagenes\Minimizar.png"), "Minimizar", self)
        boton_accion2.triggered.connect(self.minimizar)
        self.barra2.addAction(boton_accion2)
        self.barra2.setMovable(False)
        self.barra2.addWidget(izquierda)
        self.barra2.addWidget(self.titulo)
        self.barra2.addWidget(derecha)
#--------------------------------------------Fondo--------------------------------------#
        pixmap = QPixmap("Imagenes\podio.png")
        bg = QLabel(self)
        pixmap = pixmap.scaled(1200, 1200, Qt.KeepAspectRatio, Qt.FastTransformation)
        bg.setPixmap(pixmap)
        lo = QHBoxLayout()
        lo.addWidget(bg)
        widget = QWidget()
        widget.setLayout(lo)
        self.setCentralWidget(widget)

        #winner = False (Para probar las posiciones)
#------------------------------------Animales------------------------------------------------------"
        mapLiebre = QPixmap("Imagenes\Liebre.png")
        mapLiebre = mapLiebre.scaled(320, 320, Qt.KeepAspectRatio, Qt.FastTransformation)
        mapTortuga = QPixmap("Imagenes\Tortuga.png")
        mapTortuga = mapTortuga.scaled(320, 320, Qt.KeepAspectRatio, Qt.FastTransformation)
#---------------------------------Etiquteas--------------------------------#
        self.uno = QLabel(self)
        self.uno.setAttribute(Qt.WA_TranslucentBackground, True)
        self.uno.resize(320, 320)
        self.uno.move(295, 215)

        self.dos = QLabel(self)
        self.dos.setAttribute(Qt.WA_TranslucentBackground, True)
        self.dos.resize(320, 320)
        self.dos.move(650, 310)
#--------------------------Condicional de ganador--------------------------------#
        if winner == True:
            self.uno.setPixmap(mapLiebre)
            self.dos.setPixmap(mapTortuga)
        else:
            self.uno.setPixmap(mapTortuga)
            self.dos.setPixmap(mapLiebre)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
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