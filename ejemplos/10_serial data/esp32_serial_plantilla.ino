// ============================================================
// PLANTILLA EDUCATIVA ESP32 -> SERIAL
// ============================================================
// Este ejemplo envia dos valores por el puerto serial con el formato
// que espera el script Python serial_a_excel_usb.py:
// valor1,valor2
// Ejemplo:
// 24.5,60.8

// Estos valores cambian con el tiempo para simular dos sensores.
float variable1 = 20.0;
float variable2 = 50.0;

// Este tiempo controla cada cuanto se envian los datos.
const int INTERVALO_MILISEGUNDOS = 1000;


void setup() {
  // Iniciamos la comunicacion serial a la misma velocidad que usa Python.
  Serial.begin(9600);

  // Esperamos un momento para que el monitor serial y Python
  // tengan tiempo de conectarse al ESP32.
  delay(2000);

  Serial.println("ESP32 listo para enviar datos por serial.");
  Serial.println("Formato esperado por Python: valor1,valor2");
}


void loop() {
  // En una practica real, aqui podrias leer sensores reales.
  // En esta plantilla solo modificamos un poco los valores para
  // simular cambios en cada lectura.
  variable1 = variable1 + 0.4;
  variable2 = variable2 + 0.7;

  // Enviamos ambas variables en una sola linea separadas por coma.
  // Ese es el formato que Python convertira en dos columnas del Excel.
  Serial.print(variable1, 2);
  Serial.print(",");
  Serial.println(variable2, 2);

  // Esperamos antes de enviar la siguiente lectura.
  delay(INTERVALO_MILISEGUNDOS);
}