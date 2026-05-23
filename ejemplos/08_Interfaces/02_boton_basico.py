import sys

from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton, QWidget


# Este ejemplo agrega un boton y una accion al hacer clic.


def mostrar_mensaje():
    # Esta funcion se ejecuta cuando se presiona el boton.
    QMessageBox.information(ventana, "Saludo", "Hiciste clic en el boton.")


app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Ventana con boton")
ventana.resize(420, 220)


# QPushButton crea un boton visible en la ventana.
boton = QPushButton("Haz clic aqui", parent=ventana)

# resize() cambia el tamano del boton.
boton.resize(150, 40)

# move() cambia la posicion del boton dentro de la ventana.
boton.move(130, 90)


# clicked.connect(...) une el boton con la funcion que debe ejecutarse.
boton.clicked.connect(mostrar_mensaje)

ventana.show()
sys.exit(app.exec())