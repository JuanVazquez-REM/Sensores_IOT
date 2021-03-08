import sys
""" import Adafruit_DHT as dht
import RPi.GPIO as GPIO """
import time

class Sensores:

    def select_sensor(self,sensor):
        if sensor.tipo == "DHT11":
            return self.Get_Temperatura_Humedad(sensor.pin,sensor.tipo)
        elif sensor.tipo == "PIR":
            return self.Get_PIR()

    def lista_sensores(self,lista): 
        lista_lectura=[]
        
        for i in lista:
            a = self.select_sensor(i)
            lista_lectura.append(a)
        return lista_lectura

    def Get_Temperatura_Humedad(self,pin,sensor):
        sensor = dht.sensor
        humidity, temperature = dht.read_retry(sensor, pin)
        
        data = {
            'temperatura': temperature,
            'humedad': humidity
        }
        #print(temperature, humidity)
        return data

    def Get_PIR(self,pin):
        GPIO.setup(pin, GPIO.IN)
        time.sleep(1)
        
        movimiento = GPIO.input(pin)

        if movimiento == 0:    
            data={
                'response': True,
                'message': 0
            }            
            return data
        elif movimiento == 1:    
            data={
                'response': True,
                'message': 1
            }          
            return data
    
    def Get_Ultrasonico(self, pin_trigger, pin_echo):
        GPIO_TRIGGER = pin_trigger
        GPIO_ECHO = pin_echo
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
        
        return distance
        


