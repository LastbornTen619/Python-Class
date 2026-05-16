import sys

# Qt contiene constantes utiles para alineacion y orientacion.
from PySide6.QtCore import Qt

# QtWidgets incluye los controles visuales para construir la interfaz.
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QProgressBar,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Paso 1: configurar la ventana principal.
        self.setWindowTitle("Ejemplo moderno de interfaces con PySide6")
        self.resize(900, 700)

        # Paso 2: crear un contenedor central.
        # Todos los controles de la interfaz viviran dentro de este widget.
        contenedor = QWidget()
        self.setCentralWidget(contenedor)

        # Paso 3: crear el layout principal.
        # QVBoxLayout acomoda los elementos de arriba hacia abajo.
        layout_principal = QVBoxLayout()
        contenedor.setLayout(layout_principal)

        # Paso 4: agregar un titulo.
        titulo = QLabel("Formulario de ejemplo para clase")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; margin: 12px;")
        layout_principal.addWidget(titulo)

        # Paso 5: agregar cada bloque de la interfaz.
        layout_principal.addWidget(self.crear_bloque_datos())
        layout_principal.addWidget(self.crear_bloque_preferencias())
        layout_principal.addWidget(self.crear_bloque_extras())
        layout_principal.addWidget(self.crear_bloque_tabla())
        layout_principal.addWidget(self.crear_bloque_botones())

        # Paso 6: agregar una zona donde mostraremos el resultado final.
        self.etiqueta_resultado = QLabel("Aqui aparecera el resumen del formulario")
        self.etiqueta_resultado.setWordWrap(True)
        self.etiqueta_resultado.setStyleSheet(
            "background-color: #f3f4f6; padding: 12px; border-radius: 8px;"
        )
        layout_principal.addWidget(self.etiqueta_resultado)

    def crear_bloque_datos(self):
        # Este bloque agrupa los datos basicos del estudiante.
        grupo = QGroupBox("Paso 1: datos principales")
        layout = QVBoxLayout()
        grupo.setLayout(layout)

        etiqueta_nombre = QLabel("Escribe tu nombre:")
        self.entrada_nombre = QLineEdit()
        self.entrada_nombre.setPlaceholderText("Escribe tu nombre")
        layout.addWidget(etiqueta_nombre)
        layout.addWidget(self.entrada_nombre)

        etiqueta_edad = QLabel("Elige tu edad:")
        self.edad = QSpinBox()
        self.edad.setRange(10, 99)
        layout.addWidget(etiqueta_edad)
        layout.addWidget(self.edad)

        etiqueta_curso = QLabel("Selecciona tu curso favorito:")
        self.curso = QComboBox()
        self.curso.addItems(["Python", "Git", "Bases de datos", "Interfaces"])
        layout.addWidget(etiqueta_curso)
        layout.addWidget(self.curso)

        etiqueta_estado = QLabel("Marca si eres estudiante activo:")
        self.activo = QCheckBox("Estudiante activo")
        self.activo.setChecked(True)
        layout.addWidget(etiqueta_estado)
        layout.addWidget(self.activo)

        return grupo

    def crear_bloque_preferencias(self):
        # Este bloque enseña radio buttons, slider y barra de progreso.
        grupo = QGroupBox("Paso 2: preferencias")
        layout = QHBoxLayout()
        grupo.setLayout(layout)

        grupo_modalidad = QGroupBox("Modalidad")
        layout_modalidad = QVBoxLayout()
        grupo_modalidad.setLayout(layout_modalidad)

        etiqueta_modalidad = QLabel("Escoge una modalidad:")
        self.radio_presencial = QRadioButton("Presencial")
        self.radio_virtual = QRadioButton("Virtual")
        self.radio_hibrido = QRadioButton("Hibrido")
        self.radio_presencial.setChecked(True)

        layout_modalidad.addWidget(etiqueta_modalidad)
        layout_modalidad.addWidget(self.radio_presencial)
        layout_modalidad.addWidget(self.radio_virtual)
        layout_modalidad.addWidget(self.radio_hibrido)

        grupo_avance = QGroupBox("Nivel de avance")
        layout_avance = QVBoxLayout()
        grupo_avance.setLayout(layout_avance)

        etiqueta_avance = QLabel("Mueve la barra para indicar tu avance:")
        self.slider_avance = QSlider(Qt.Horizontal)
        self.slider_avance.setRange(0, 100)
        self.slider_avance.setValue(50)

        self.barra_avance = QProgressBar()
        self.barra_avance.setRange(0, 100)
        self.barra_avance.setValue(50)

        # Cuando el slider cambia, la barra de progreso tambien cambia.
        self.slider_avance.valueChanged.connect(self.barra_avance.setValue)

        layout_avance.addWidget(etiqueta_avance)
        layout_avance.addWidget(self.slider_avance)
        layout_avance.addWidget(self.barra_avance)

        layout.addWidget(grupo_modalidad)
        layout.addWidget(grupo_avance)

        return grupo

    def crear_bloque_extras(self):
        # Este bloque muestra una lista y un area de texto.
        grupo = QGroupBox("Paso 3: extras de la interfaz")
        layout = QHBoxLayout()
        grupo.setLayout(layout)

        columna_izquierda = QVBoxLayout()
        columna_derecha = QVBoxLayout()

        self.habilidades = QListWidget()
        self.habilidades.addItems(
            ["Variables", "Condicionales", "Bucles", "Funciones", "Git"]
        )

        self.notas = QTextEdit()
        self.notas.setPlaceholderText("Escribe observaciones o comentarios")

        columna_izquierda.addWidget(QLabel("Lista de habilidades:"))
        columna_izquierda.addWidget(self.habilidades)

        columna_derecha.addWidget(QLabel("Area de texto:"))
        columna_derecha.addWidget(self.notas)

        layout.addLayout(columna_izquierda)
        layout.addLayout(columna_derecha)

        return grupo

    def crear_bloque_tabla(self):
        # Este bloque muestra una tabla sencilla con datos de ejemplo.
        grupo = QGroupBox("Paso 4: tabla de ejemplo")
        layout = QVBoxLayout()
        grupo.setLayout(layout)

        self.tabla = QTableWidget(3, 2)
        self.tabla.setHorizontalHeaderLabels(["Actividad", "Calificacion"])

        datos = [
            ("Ejercicio 1", "95"),
            ("Ejercicio 2", "88"),
            ("Proyecto", "100"),
        ]

        for fila, (actividad, calificacion) in enumerate(datos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(actividad))
            self.tabla.setItem(fila, 1, QTableWidgetItem(calificacion))

        layout.addWidget(self.tabla)
        return grupo

    def crear_bloque_botones(self):
        # Este bloque contiene los botones que ejecutan acciones.
        layout = QHBoxLayout()

        boton_resumen = QPushButton("Mostrar resumen")
        boton_resumen.clicked.connect(self.mostrar_resumen)

        boton_limpiar = QPushButton("Limpiar formulario")
        boton_limpiar.clicked.connect(self.limpiar_formulario)

        layout.addWidget(boton_resumen)
        layout.addWidget(boton_limpiar)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        return contenedor

    def obtener_modalidad(self):
        # Esta funcion revisa cual radio button esta seleccionado.
        if self.radio_presencial.isChecked():
            return "Presencial"
        if self.radio_virtual.isChecked():
            return "Virtual"
        return "Hibrido"

    def mostrar_resumen(self):
        # Esta funcion toma los datos actuales de la ventana y arma un resumen.
        nombre = self.entrada_nombre.text().strip() or "Sin nombre"
        modalidad = self.obtener_modalidad()
        habilidad_actual = self.habilidades.currentItem()
        habilidad = habilidad_actual.text() if habilidad_actual else "Ninguna"

        resumen = (
            f"Nombre: {nombre}\n"
            f"Edad: {self.edad.value()}\n"
            f"Curso favorito: {self.curso.currentText()}\n"
            f"Activo: {'Si' if self.activo.isChecked() else 'No'}\n"
            f"Modalidad: {modalidad}\n"
            f"Avance: {self.slider_avance.value()}%\n"
            f"Habilidad seleccionada: {habilidad}\n"
            f"Notas: {self.notas.toPlainText() or 'Sin comentarios'}"
        )

        # Mostramos el resumen dentro de la misma ventana.
        self.etiqueta_resultado.setText(resumen)

        # Tambien lo mostramos en una ventana emergente.
        QMessageBox.information(self, "Resumen", resumen)

    def limpiar_formulario(self):
        # Esta funcion regresa todos los controles a su valor inicial.
        self.entrada_nombre.clear()
        self.edad.setValue(10)
        self.curso.setCurrentIndex(0)
        self.activo.setChecked(True)
        self.radio_presencial.setChecked(True)
        self.slider_avance.setValue(50)
        self.habilidades.clearSelection()
        self.notas.clear()
        self.etiqueta_resultado.setText("Aqui aparecera el resumen del formulario")


def main():
    # QApplication inicia la aplicacion grafica.
    app = QApplication(sys.argv)

    # Creamos la ventana principal.
    ventana = VentanaPrincipal()

    # Mostramos la ventana en pantalla.
    ventana.show()

    # app.exec() mantiene la aplicacion abierta hasta que el usuario la cierre.
    sys.exit(app.exec())


if __name__ == "__main__":
    main()