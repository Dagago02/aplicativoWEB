import serial
import json

# Configura la conexión serial (ajusta el puerto COM según tu configuración)
arduino_port = 'COM6'  # Reemplaza 'COMX' con el puerto correcto
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)

# Crea un diccionario para almacenar los datos
data = {}

try:
    while True:
        # Lee una línea de datos desde el Arduino
        line = ser.readline().decode().strip()

        # Divide la línea en valores separados por comas
        values = line.split(',')

        if len(values) == 7:  # Asegúrate de que haya 7 valores
            dato1, dato2, dato3, dato4, dato5, dato6, dato7 = map(int, values)

            # Almacena los datos en el diccionario
            data['dato1'] = dato1
            data['dato2'] = dato2
            data['dato3'] = dato3
            data['dato4'] = dato4
            data['dato5'] = dato5
            data['dato6'] = dato6
            data['dato7'] = dato7

            # Escribe el diccionario en un archivo JSON
            with open('datos.json', 'w') as json_file:
                json.dump(data, json_file)
                print("Datos escritos en datos.json")

except KeyboardInterrupt:
    ser.close()
    print("Conexión cerrada")
