# Serial Data A Excel Y Graficas

Estos ejemplos sirven como plantilla educativa para aprender a:

1. Leer datos desde un microcontrolador por puerto serial.
2. Guardar dos variables en un archivo Excel.
3. Leer ese Excel y crear una grafica.
4. Usar un ESP32 como emisor de datos de prueba.

## Librerias necesarias en Python

```bash
python -m pip install pyserial pandas openpyxl matplotlib
```

## Archivos

1. `serial_a_excel_usb.py`: abre el puerto serial y guarda dos columnas en `lecturas_serial.xlsx`.
2. `graficar_excel_serial.py`: lee el Excel y genera una grafica.
3. `esp32_serial_plantilla.ino`: ejemplo para ESP32 que envia dos variables con el formato que espera Python.

## Formato esperado desde el ESP32

Cada linea debe tener dos valores separados por coma:

```text
24.5,60.8
```

## Uso sugerido

1. Carga `esp32_serial_plantilla.ino` en el ESP32.
2. Revisa el puerto `COM` correcto en `serial_a_excel_usb.py`.
3. Ejecuta `serial_a_excel_usb.py` para crear `lecturas_serial.xlsx`.
4. Ejecuta `graficar_excel_serial.py` para generar la grafica.