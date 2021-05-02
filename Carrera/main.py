import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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

        self.titulo = QLabel("                                                                                                                                       Carrera")
        self.titulo.setFont(QFont("Segoe UI Light", 12))
        self.barra = QToolBar("barra de herramientas")
        self.barra.setIconSize(QSize(16, 16))
        self.addToolBar(self.barra)
        self.barra.setStyleSheet("background: rgb(165,165,165,250); color: white; border-top-right-radius: 8px;"
                                 "border-top-right-radius: 8px;"
                                 "border-bottom-left-radius: 0px;"
                                 "border-bottom-right-radius: 0px")

 #---------------------------------Barra de tareas----------------------------------#
        boton_accion = QAction(QIcon("Imagenes\Cerrar.png"), "Cerrar", self)
        boton_accion.triggered.connect(self.cerrar)
        self.barra.addAction(boton_accion)

        boton_accion2 = QAction(QIcon("Imagenes\Minimizar.png"), "Minimizar", self)
        boton_accion2.triggered.connect(self.minimizar)
        self.barra.addAction(boton_accion2)
        self.barra.setMovable(False)
        self.barra.addWidget(self.titulo)

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
    
        #Prueba = QPushButton(self)
        #botn = QPixmap("Imagenes\Boton.png")
        #ico = QIcon(botn)
        #Prueba.setIcon(ico)
        #Prueba.setAttribute(Qt.WA_TranslucentBackground, True)
        #Prueba.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #Prueba.setIconSize(pixmap.rect().size())
        #Prueba.resize(212, 200)
        #Prueba.setStyleSheet("border-radius: 5px; color: white; background: rgb(165,165,165); border: 2px solid white;")
        #Prueba.move(950 / 2 - 150 / 2, 780 / 2 - 40 / 2)

# ------------------------------------------Titulo------------------------------------------------#
        pixmap = QPixmap("Imagenes\Carrera.png")
        titulo = QLabel(self)
        pixmap = pixmap.scaled(1000, 1000, Qt.KeepAspectRatio, Qt.FastTransformation)
        titulo.setAttribute(Qt.WA_TranslucentBackground, True)
        titulo.setPixmap(pixmap)
        titulo.resize(1000, 1000)
        titulo.move(370 / 2 - 150 / 2, - 540 / 2 - 40 / 2)

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