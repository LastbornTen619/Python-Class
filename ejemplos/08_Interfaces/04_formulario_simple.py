import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# Este ejemplo junta varios conceptos:
# 1. Una etiqueta
# 2. Una caja de texto
# 3. Un boton
# 4. Un area donde se muestra el resultado


def saludar():
    # text() lee lo que el usuario escribio en la caja.
    nombre = entrada_nombre.text().strip()

    if nombre:
        resultado.setText(f"Hola, {nombre}. Bienvenido a PySide6.")
    else:
        resultado.setText("Escribe tu nombre antes de presionar el boton.")


app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Formulario simple")
ventana.resize(460, 220)


# Layout principal: apila bloques de arriba hacia abajo.
layout_principal = QVBoxLayout()


# Layout horizontal para poner la etiqueta y la caja de texto en una sola fila.
fila_nombre = QHBoxLayout()

etiqueta_nombre = QLabel("Nombre:")


# QLineEdit crea una caja donde el usuario puede escribir.
entrada_nombre = QLineEdit()
entrada_nombre.setPlaceholderText("Escribe tu nombre aqui")

fila_nombre.addWidget(etiqueta_nombre)
fila_nombre.addWidget(entrada_nombre)


# Boton que activa la funcion saludar().
boton_saludar = QPushButton("Saludar")
boton_saludar.clicked.connect(saludar)


# Etiqueta donde mostraremos el resultado.
resultado = QLabel("Aqui aparecera el mensaje.")


layout_principal.addLayout(fila_nombre)
layout_principal.addWidget(boton_saludar)
layout_principal.addWidget(resultado)

ventana.setLayout(layout_principal)

ventana.show()
sys.exit(app.exec())