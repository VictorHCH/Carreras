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

        self.titulo = QLabel("            Carrera")
        self.titulo.setFont(QFont("Segoe UI Light", 12))
        self.barra = QToolBar("barra de herramientas")
        self.barra.setIconSize(QSize(16, 16))
        self.addToolBar(self.barra)
        self.barra.setStyleSheet("background: rgb(165,165,165,250); color: white; border-top-right-radius: 8px;"
                                 "border-top-right-radius: 8px;"
                                 "border-bottom-left-radius: 0px;"
                                 "border-bottom-right-radius: 0px")

        boton_accion = QAction(QIcon("Imagenes\Cerrar.png"), "Cerrar", self)
        boton_accion.triggered.connect(self.cerrar)
        self.barra.addAction(boton_accion)

        boton_accion2 = QAction(QIcon("Imagenes\Minimizar.png"), "Minimizar", self)
        boton_accion2.triggered.connect(self.minimizar)
        self.barra.addAction(boton_accion2)


        self.barra.setMovable(False)
        self.barra.addWidget(self.titulo)

        text = QLabel("Bienvenido")
        text2 = QLabel("Esta es una alfa!")
        lo = QHBoxLayout()
        lo.addWidget(text)
        lo.addWidget(text2)
        widget = QWidget()
        widget.setLayout(lo)
        self.setCentralWidget(widget)

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