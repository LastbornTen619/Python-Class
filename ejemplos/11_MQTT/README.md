# MQTT A Excel Y Graficas Con Mosquitto

Estos ejemplos sirven como plantilla educativa para aprender a:

1. Conectarse a un broker Mosquitto en una PC con Ubuntu.
2. Suscribirse a un topico de sensores.
3. Publicar comandos a un topico del ESP32.
4. Guardar mensajes recibidos en un archivo Excel.
5. Leer ese Excel y crear una grafica.
6. Usar un ESP32 como cliente MQTT para enviar datos reales.

## Librerias necesarias

```bash
python -m pip install paho-mqtt pandas openpyxl matplotlib
```

## Archivos

1. `mqtt_a_excel.py`: se conecta al broker Mosquitto, se suscribe al topico de sensores, publica un comando de prueba y guarda lo recibido en `lecturas_mqtt.xlsx`.
2. `graficar_excel_mqtt.py`: lee el Excel y crea una grafica en pantalla y como imagen.
3. `esp32_mqtt_plantilla.ino`: ejemplo para ESP32 que se conecta al WiFi, publica dos valores por MQTT y escucha comandos.

## Flujo de trabajo

1. Mosquitto corre en tu PC con Ubuntu.
2. El ESP32 se conecta al WiFi y publica en `clase/esp32/sensores`.
3. Python se suscribe a `clase/esp32/sensores` y guarda los datos en Excel.
4. Python puede publicar un comando en `clase/esp32/comandos`.
5. El ESP32 recibe ese comando y lo muestra en el monitor serial.

## Instalar Mosquitto En Ubuntu

```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
sudo systemctl status mosquitto
```

## Ver La IP De Ubuntu

```bash
hostname -I
```

Usa esa IP en estos dos archivos:

1. `mqtt_a_excel.py`
2. `esp32_mqtt_plantilla.ino`

## Pruebas Rapidas En Ubuntu

Abrir una terminal para escuchar mensajes:

```bash
mosquitto_sub -h localhost -t clase/esp32/sensores
```

Abrir otra terminal para enviar un comando al ESP32:

```bash
mosquitto_pub -h localhost -t clase/esp32/comandos -m "ENCENDER_LED"
```

## Nota Sobre Red Local

1. El ESP32, la PC Ubuntu y la PC donde corre Python deben estar en la misma red.
2. Si Ubuntu tiene firewall activo, hay que permitir el puerto `1883`.

## Uso sugerido

1. Instala y arranca Mosquitto en Ubuntu.
2. Coloca la IP de Ubuntu en `mqtt_a_excel.py` y en `esp32_mqtt_plantilla.ino`.
3. Carga `esp32_mqtt_plantilla.ino` en el ESP32.
4. Ejecuta `mqtt_a_excel.py` para generar el Excel.
5. Revisa el archivo `lecturas_mqtt.xlsx`.
6. Ejecuta `graficar_excel_mqtt.py` para generar la grafica.