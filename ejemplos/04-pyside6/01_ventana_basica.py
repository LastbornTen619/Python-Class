import sys

from PySide6.QtWidgets import QApplication, QLabel, QWidget


# Este archivo muestra el ejemplo mas simple posible.
# La idea es entender como se abre una ventana.


# QApplication prepara la aplicacion grafica.
# Sin esto, la ventana no puede funcionar.
app = QApplication(sys.argv)


# QWidget crea una ventana vacia basica.
ventana = QWidget()

# Esto cambia el texto que aparece arriba en la barra de la ventana.
ventana.setWindowTitle("Mi primera ventana con PySide6")

# Esto cambia el ancho y el alto inicial de la ventana.
ventana.resize(420, 220)


# QLabel crea un texto visible dentro de la ventana.
mensaje = QLabel("Hola. Esta es una ventana basica.", parent=ventana)

# move(x, y) cambia la posicion del texto dentro de la ventana.
mensaje.move(90, 95)


# show() hace visible la ventana en pantalla.
ventana.show()


# exec() mantiene la app abierta hasta que el usuario la cierre.
sys.exit(app.exec())