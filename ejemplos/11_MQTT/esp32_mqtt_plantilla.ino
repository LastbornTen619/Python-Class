// ============================================================
// PLANTILLA EDUCATIVA ESP32 -> MQTT
// ============================================================
// Este ejemplo conecta el ESP32 a WiFi y publica dos valores en el topico
// que espera la plantilla Python mqtt_a_excel.py.
//
// Formato del mensaje:
// valor1,valor2
// Ejemplo:
// 24.5,60.8

#include <WiFi.h>
#include <PubSubClient.h>


// ============================================================
// CONFIGURACION WIFI Y MQTT
// ============================================================
// Cambia estos valores por los de tu red y por la IP de tu PC Ubuntu.
const char* WIFI_SSID = "TU_WIFI";
const char* WIFI_PASSWORD = "TU_PASSWORD";

const char* BROKER_MQTT = "192.168.1.100";
const int PUERTO_MQTT = 1883;
const char* TOPICO_PUBLICACION = "clase/esp32/sensores";
const char* TOPICO_SUSCRIPCION = "clase/esp32/comandos";


WiFiClient clienteWifi;
PubSubClient clienteMqtt(clienteWifi);

float variable1 = 20.0;
float variable2 = 50.0;
unsigned long ultimoEnvio = 0;
const unsigned long INTERVALO_MILISEGUNDOS = 2000;


void conectarWifi() {
  Serial.print("Conectando a WiFi");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi conectado correctamente.");
  Serial.print("IP local: ");
  Serial.println(WiFi.localIP());
}


void mensajeRecibido(char* topico, byte* payload, unsigned int length) {
  // Esta funcion muestra los mensajes que llegan al topico suscrito.
  // Sirve para explicar que el ESP32 tambien puede recibir comandos.
  Serial.print("Mensaje recibido en ");
  Serial.print(topico);
  Serial.print(": ");

  for (unsigned int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }

  Serial.println();

  // Aqui puedes agregar acciones reales segun el comando recibido.
  // Por ejemplo, encender un LED o cambiar el intervalo de envio.
}


void conectarMqtt() {
  // Si se pierde la conexion, este bloque intenta reconectarse.
  while (!clienteMqtt.connected()) {
    Serial.print("Conectando al broker MQTT...");

    String clientId = "esp32-clase-";
    clientId += String((uint32_t)ESP.getEfuseMac(), HEX);

    if (clienteMqtt.connect(clientId.c_str())) {
      Serial.println("conectado.");
      clienteMqtt.subscribe(TOPICO_SUSCRIPCION);
      Serial.print("Suscrito a: ");
      Serial.println(TOPICO_SUSCRIPCION);
    } else {
      Serial.print("fallo, rc=");
      Serial.print(clienteMqtt.state());
      Serial.println(". Reintentando en 2 segundos...");
      delay(2000);
    }
  }
}


void publicarLectura() {
  // En un proyecto real, aqui podrias leer sensores de temperatura,
  // humedad, distancia, luz u otras variables.
  variable1 = variable1 + 0.5;
  variable2 = variable2 + 0.8;

  // Construimos el mensaje exactamente con el formato que espera Python.
  String mensaje = String(variable1, 2) + "," + String(variable2, 2);

  clienteMqtt.publish(TOPICO_PUBLICACION, mensaje.c_str());

  Serial.print("Publicado en ");
  Serial.print(TOPICO_PUBLICACION);
  Serial.print(": ");
  Serial.println(mensaje);
}


void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("Plantilla ESP32 + Mosquitto local");
  Serial.println("El broker debe ser la IP de tu PC Ubuntu en la misma red.");

  conectarWifi();

  clienteMqtt.setServer(BROKER_MQTT, PUERTO_MQTT);
  clienteMqtt.setCallback(mensajeRecibido);
}


void loop() {
  if (!clienteMqtt.connected()) {
    conectarMqtt();
  }

  clienteMqtt.loop();

  // Publicamos una lectura cada cierto tiempo.
  if (millis() - ultimoEnvio >= INTERVALO_MILISEGUNDOS) {
    ultimoEnvio = millis();
    publicarLectura();
  }
}