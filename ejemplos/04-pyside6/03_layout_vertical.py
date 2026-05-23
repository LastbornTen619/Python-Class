import sys

from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


# Este ejemplo muestra una forma mejor de ordenar elementos.
# En lugar de usar move(), usamos un layout vertical.


app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Ventana con layout vertical")
ventana.resize(420, 260)


# QVBoxLayout acomoda los elementos uno debajo del otro.
layout = QVBoxLayout()


# Creamos varios widgets para meterlos dentro del layout.
titulo = QLabel("Ejemplo de layout vertical")
texto = QLabel("Los elementos se acomodan solos en columna.")
boton_1 = QPushButton("Boton 1")
boton_2 = QPushButton("Boton 2")


# addWidget() agrega cada elemento al layout.
layout.addWidget(titulo)
layout.addWidget(texto)
layout.addWidget(boton_1)
layout.addWidget(boton_2)


# setLayout() coloca el layout dentro de la ventana.
ventana.setLayout(layout)

ventana.show()
sys.exit(app.exec())