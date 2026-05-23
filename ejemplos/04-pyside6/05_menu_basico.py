import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox


# Este ejemplo usa QMainWindow, una ventana mas completa.
# Sirve para aprender a crear una barra de menu.


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Esto cambia el titulo de la ventana.
        self.setWindowTitle("Ventana con menu")

        # Esto cambia el ancho y el alto inicial.
        self.resize(520, 280)

        # QLabel crea un texto en la parte central de la ventana.
        mensaje = QLabel(
            "Mira arriba: esta ventana tiene una barra de menu.",
            self,
        )

        # setCentralWidget() pone un widget principal en el centro.
        self.setCentralWidget(mensaje)

        # menuBar() crea u obtiene la barra de menu superior.
        barra_menu = self.menuBar()

        # addMenu() crea una opcion principal del menu.
        menu_archivo = barra_menu.addMenu("Archivo")
        menu_ayuda = barra_menu.addMenu("Ayuda")

        # QAction crea una accion que luego se agrega al menu.
        accion_saludar = QAction("Mostrar saludo", self)
        accion_saludar.triggered.connect(self.mostrar_saludo)

        accion_salir = QAction("Salir", self)
        accion_salir.triggered.connect(self.close)

        accion_acerca = QAction("Acerca de", self)
        accion_acerca.triggered.connect(self.mostrar_acerca_de)

        # addAction() mete cada accion dentro del menu elegido.
        menu_archivo.addAction(accion_saludar)
        menu_archivo.addAction(accion_salir)
        menu_ayuda.addAction(accion_acerca)

    def mostrar_saludo(self):
        # Esto abre una ventana pequena con un mensaje.
        QMessageBox.information(self, "Saludo", "Elegiste la opcion Mostrar saludo.")

    def mostrar_acerca_de(self):
        # Este mensaje explica para que sirve el ejemplo.
        QMessageBox.information(
            self,
            "Acerca de",
            "Este ejemplo muestra como crear una barra de menu en PySide6.",
        )


app = QApplication(sys.argv)

# Creamos la ventana principal de la aplicacion.
ventana = VentanaPrincipal()

# show() la hace visible.
ventana.show()

# exec() deja la app activa hasta que se cierre.
sys.exit(app.exec())