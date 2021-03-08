import sys
import Adafruit_DHT as dht
import RPi.GPIO as GPIO 
import time

class Sensores:

    def sensor(self, data):
        response = {'status': False, 'message':None}
        try:
            if data['sensor'] == "TEMPERATURA_HUMEDAD":
                return self.Get_Temperatura_Humedad(data)
            elif data['sensor'] == "PIR":
                return self.Get_PIR(data)
            elif data['sensor'] == "ULTRASONICO":
                print("ULTRASONICO")
            else:
                response['message'] = "Sensor no encontrado"
                return response

        except Exception as e:
            response['message'] = e
            return response

    def Get_Temperatura_Humedad(self,data):
        response = {'status': False, 'message':None}

        if data['tipo'] == "DHT11":
            sensor = dht.DHT11
        elif data['tipo'] == "DHT22":
            sensor = dht.DHT22
        else:
            reponse['message'] = "Tipo de sensor temperatura no encontrado"
            return response
        
        try:
            GPIO.setup(data['pin'], GPIO.IN)
            humidity,temperature = dht.read_retry(sensor, data['pin'])
            response['status'] = True
            response['message'] = {'humedad':humidity,'temperatura':temperature}
            return response
            
        except Exception as e:
            response['message'] = e
            return response


    """ def lista_sensores(self,lista): 
        lista_lectura=[]
        
        for i in lista:
            a = self.select_sensor(i)
            lista_lectura.append(a)
        return lista_lectura """

    def Get_PIR(self,data):
        response = {'status': False, 'message':None}
        try:
            GPIO.setup(data['pin'], GPIO.IN)
            time.sleep(1)
            movimiento = GPIO.input(data['pin'])
            
            response['status'] = True
            if movimiento == 0:
                response['message'] = 0
                return response
            elif movimiento == 1:    
                response['message'] = 1 
                return response
        except Exception as e:
            response['message'] = e
            return response

    def Get_Ultrasonico(self, data):
        response = {'status': False, 'message':None}
        try:
            GPIO_TRIGGER = data['pin_trigger']
            GPIO_ECHO = data['pin_echo']

            GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
            GPIO.setup(GPIO_ECHO, GPIO.IN)

            GPIO.output(GPIO_TRIGGER, True)
            
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIGGER, False)        
            StartTime = time.time()
            StopTime = time.time()

            while GPIO.input(GPIO_ECHO) == 0:
                StartTime = time.time()
            
            while GPIO.input(GPIO_ECHO) == 1:
                StopTime = time.time()
            
            TimeElapsed = StopTime - StartTime
            distance = (TimeElapsed * 34300) / 2

            response['status'] = True
            response['message'] = distance
            return response
        except Exception as e:
            response['message'] = e
            return response



