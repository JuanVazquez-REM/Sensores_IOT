from typing import Collection
from Sensores import Sensores
from Mongo import Database2
from Mysql import Mysql
from datetime import datetime
def menu():
    print("------------")
    print("1-Sensor Temperatura Y Humedad")
    print("2-Sensor PIR")
    print("3-Sensor Ultrasonico")
    print("4-Salir")
    print("------------")

ciclo = True
while ciclo:
    menu()
    opcion = input("Elije la opcion: ")

    if opcion == "1":
        ciclo2 = True
        while ciclo2:
            print("------------Menu Sensor Temperatura y humedad------------")
            print("1-Calcular Tempratura y humedad")
            print("2-Mostrar ultimo dato registrado")
            print("3-Mostrar todos los datos registrados")
            print("4-Salir")
            print("------------")
            opcion = input("Elije una opcion: ")
            
            if opcion == "1":#Calcular Tempratura y humedad
                #CALCULANDO TEMPERATURA Y HUMEDAD
                Sensor = Sensores()
                data = {
                    'sensor': "TEMPERATURA_HUMEDA",
                    'tipo': "DHT11",
                    'pin': 4
                }
                print("Calculando Temperatura y Humedad...")
                response = Sensor.sensor(data)
                print(data['message'])
                #CALCULANDO TEMPERATURA Y HUMEDAD
                
                print("Guardando datos en...")
                #GUARDANDO DATOS EN MYSQL
                mysql = Mysql('localhost','administrador','admin','sensores_python')
                sql = 'INSERT INTO valores (sensor,temperatura, humedad, fecha) VALUES ('+ 1 +','+ data['message'].temperatura +', '+ data['message'].humedad +','+datetime.now()+');'
                mysql.commit(sql)
                mysql.close()
                #GUARDANDO DATOS EN MYSQL
                print("Mysql...")

                #GUARDANDO DATOS EN MONGODB
                #CARLOS
                mongo = Database2('localhost','Sensores','Temperatura_Humedad',27017)
                db = mongo.Temperatura_Humedad
                collection = db.Sensores
                collection.insert_one({"Temperatura" ,"Humedad"})
                
                #GUARDANDO DATOS EN MONGODB
                print("Mongo...")
                


                #GUARDANDO DATOS EN UN ARCHIVO
                #ROSA
                #GUARDANDO DATOS EN UN ARCHIVO
                print("Archivo...")


            elif opcion == "2":#Mostrar ultimo dato registrado
                sql = 'SELECT * FROM sensores INNER JOIN valores on sensores.id = valores.sensor_id where sensores.sensor="TEMPERATURA_HUMEDAD" order by id DESC LIMIT 1'
                #CONSULTA EN MYSQL
                resultado = Mysql('localhost','administrador','admin','sensores_python')
                dato = resultado.select(sql,True)
                print("Resultado Mysql")
                print()
                print("Id: ", dato[0])
                print("Temperatura: ", dato[2])
                print("Humedad: ", dato[3])
                print("Fecha: ", dato[6])
                #CONSULTA EN MYSQL

                #CONSULTA EN MONGODB
                mongo = Database2('localhost','Sensores','Temperatura_Humedad',27017)
                db = mongo.Temperatura_Humedad
                collection = db.Sensores
                collection.find().sort({"$natural":-1}).limit(1).pretty()
                print("Temperatura" ) #no logro buscar algo que me ayude
                print("Humedad" ) #duda
                print("Resultado Mongo")
                print()
                
                #CONSULTA EN ARCHIVO
                #ROSA
                print("Resultado Archivo")
                print()
                #CONSULTA EN ARCHIVO
            
            elif opcion == "3":#Mostrar todos los datos registrados
                #CONSULTA EN MYSQL
                sql = 'SELECT * FROM sensores INNER JOIN values on sensores.id = values.sensor_id WHERE sensores.sensor="TEMPERATURA_HUMEDAD"'
                query = Mysql('localhost','administrador','admin','sensores_python')
                resultados = query.select(sql)
                print("Resultado mysql")
                print()
                for columna in resultados:
                    print("_____")
                    print("Id: ", columna[0])
                    print("Temperatura: ", columna[2])
                    print("Humedad: ", columna[3])
                    print("Fecha: ", columna[6])
                    print("_____\n")
                query.close()
                #CONSULTA EN MYSQL

                #CONSULTA EN MONGO
                #CARLOS
                
                mongo = Database2('localhost','Sensores','Temperatura_Humedad',27017)
                db = mongo.Temperatura_Humedad
                collection = db.Sensores
                collection.find().pretty()
                print("Resultado MONGODB")
                print()
                for col in collection:
                    print("_____")
                    print("Id: ", )
                    print("Temperatura: ", )
                    print("Humedad: ", )
                    print("_____\n")
                
                #CONSULTA EN MONGO

                #CONSULTA EN ARCHIVO
                #ROSA
                print("Resultado Archivo")
                print()
                #CONSULTA EN ARCHIVO
            elif opcion == "4":
                ciclo2 = False

    elif opcion == "2":
        ciclo2 = True
        while ciclo2:
            print("------------Menu Sensor Pir------------")
            print("1-Calcular PIR")
            print("2-Mostrar ultimo dato registrado")
            print("3-Mostrar todos los datos registrados")
            print("4-Salir")
            print("------------")
            opcion = input("Elije una opcion: ")
            
            if opcion == "1":#Calcular PIR
                #CALCULANDO PIR
                Sensor = Sensores()
                data = {
                    'sensor': "PIR",
                    'pin': 5
                }
                print("Calculando PIR...")
                response = Sensor.sensor(data)
                print("MOVIMIENTO: "+data['message'])
                #CALCULANDO PIR
                
                print("Guardando datos en...")
                #GUARDANDO DATOS EN MYSQL
                mysql = Mysql('localhost','administrador','admin','sensores_python')
                sql = 'INSERT INTO valores (sensor,movimiento,fecha) VALUES ('+ 2 +','+ data['message'] +','+datetime.now()+');'
                mysql.commit(sql)
                mysql.close()
                #GUARDANDO DATOS EN MYSQL
                print("Mysql...")

                #GUARDANDO DATOS EN MONGODB
                #CARLOS
                
                mongo = Database2('localhost','Sensores','PIR',27017)
                db = mongo.PIR
                collection = db.Sensores
                collection.insert_one({"Movimiento" ,"Fecha" })
                print("Mongo...")
                

                #GUARDANDO DATOS EN UN ARCHIVO
                #ROSA
                #GUARDANDO DATOS EN UN ARCHIVO
                print("Archivo...")


            elif opcion == "2":#Mostrar ultimo dato registrado
                sql = 'SELECT * FROM sensores INNER JOIN valores on sensores.id = valores.sensor_id where sensores.sensor="PIR" order by id DESC LIMIT 1'
                #CONSULTA EN MYSQL
                resultado = Mysql('localhost','administrador','admin','sensores_python')
                dato = resultado.select(sql,True)
                print("Resultado Mysql")
                print()
                print("Id: ", dato[0])
                print("Movimiento: ", dato[4])
                print("Fecha: ", dato[6])
                #CONSULTA EN MYSQL

                #CONSULTA EN MONGODB
                #CARLOS
                mongo = Database2('localhost','Sensores','PIR',27017)
                db = mongo.PIR
                collection = db.Sensores
                collection.find().sort({"$natural":-1}).limit(1).pretty()
                print("Movimiento" ) #no logro buscar algo que me ayude
                print("Fecha" )
                print("Resultado Mongo")
                print()
                #CONSULTA EN MONGODB
                
                #CONSULTA EN ARCHIVO
                #ROSA
                print("Resultado Archivo")
                print()
                #CONSULTA EN ARCHIVO
            
            elif opcion == "3":#Mostrar todos los datos registrados
                #CONSULTA EN MYSQL
                sql = 'SELECT * FROM sensores INNER JOIN values on sensores.id = values.sensor_id WHERE sensores.sensor="PIR"'
                query = Mysql('localhost','administrador','admin','sensores_python')
                resultados = query.select(sql)
                print("Resultado mysql")
                print()
                for columna in resultados:
                    print("_____")
                    print("Id: ", columna[0])
                    print("movimiento: ", columna[4])
                    print("Fecha: ", columna[6])
                    print("_____\n")
                query.close()
                #CONSULTA EN MYSQL

                #CONSULTA EN MONGO
                #CARLOS
                mongo = Database2('localhost','Sensores','PIR',27017)
                db = mongo.PIR
                collection = db.Sensores
                collection.find().pretty()
                
                for col in collection:
                    print("_____")
                    print("Movimiento: ", )
                    print("Fecha: ", )
                    print("_____\n")
                print("Resultado MONGODB")
                print()
                #CONSULTA EN MONGO

                #CONSULTA EN ARCHIVO
                #ROSA
                print("Resultado Archivo")
                print()
                #CONSULTA EN ARCHIVO
            elif opcion == "4":
                ciclo2 = False

    elif opcion == "3":
        ciclo2 = True
        while ciclo2:
            print("------------Menu Sensor Ultrasonico------------")
            print("1-Calcular ULTRASONICO")
            print("2-Mostrar ultimo dato registrado")
            print("3-Mostrar todos los datos registrados")
            print("4-Salir")
            print("------------")
            opcion = input("Elije una opcion: ")
            
            if opcion == "1":#Calcular ULTRASONICO
                #Calcular ULTRASONICO
                Sensor = Sensores()
                data = {
                    'sensor': "ULTRASONICO",
                    'pin_trigger': 6,
                    'pin_echo': 7
                }
                print("Calculando ULTRASONICO...")
                response = Sensor.sensor(data)
                print("DISTANCIA: "+data['message'])
                #Calcular ULTRASONICO
                
                print("Guardando datos en...")
                #GUARDANDO DATOS EN MYSQL
                mysql = Mysql('localhost','administrador','admin','sensores_python')
                sql = 'INSERT INTO valores (sensor,distancia,fecha) VALUES ('+ 3 +','+ data['message'] +','+datetime.now()+');'
                mysql.commit(sql)
                mysql.close()
                #GUARDANDO DATOS EN MYSQL
                print("Mysql...")

                #GUARDANDO DATOS EN MONGODB
                #CARLOS
                #GUARDANDO DATOS EN MONGODB
                mongo = Database2('localhost','Sensores','Ultra_sonico',27017)
                db = mongo.Ultra_sonico
                collection = db.Sensores
                collection.insert_one({"Distancia" ,"Fecha" })
                print("Mongo...")
                

                #GUARDANDO DATOS EN UN ARCHIVO
                #ROSA
                #GUARDANDO DATOS EN UN ARCHIVO
                print("Archivo...")


            elif opcion == "2":#Mostrar ultimo dato registrado
                sql = 'SELECT * FROM sensores INNER JOIN valores on sensores.id = valores.sensor_id where sensores.sensor="ULTRASONICO" order by id DESC LIMIT 1'
                #CONSULTA EN MYSQL
                resultado = Mysql('localhost','administrador','admin','sensores_python')
                dato = resultado.select(sql,True)
                print("Resultado Mysql")
                print()
                print("Id: ", dato[0])
                print("Distancia: ", dato[5])
                print("Fecha: ", dato[6])
                #CONSULTA EN MYSQL

                #CONSULTA EN MONGODB
                #CARLOS
                mongo = Database2('localhost','Sensores','Ultra_sonico',27017)
                db = mongo.Ultra_sonico
                collection = db.Sensores
                collection.find().sort({"$natural":-1}).limit(1).pretty()
                print("Movimiento" ) #no logro buscar algo que me ayude
                print("Fecha" )
                print("Resultado Mongo")
                print()
                #CONSULTA EN MONGODB
                
                #CONSULTA EN ARCHIVO
                #ROSA
                print("Resultado Archivo")
                print()
                #CONSULTA EN ARCHIVO
            
            elif opcion == "3":#Mostrar todos los datos registrados
                #CONSULTA EN MYSQL
                sql = 'SELECT * FROM sensores INNER JOIN values on sensores.id = values.sensor_id WHERE sensores.sensor="ULTRASONICO"'
                query = Mysql('localhost','administrador','admin','sensores_python')
                resultados = query.select(sql)
                print("Resultado mysql")
                print()
                for columna in resultados:
                    print("_____")
                    print("Id: ", columna[0])
                    print("Distancia: ", columna[5])
                    print("Fecha: ", columna[6])
                    print("_____\n")
                query.close()
                #CONSULTA EN MYSQL

                #CONSULTA EN MONGO
                #CARLOS
                mongo = Database2('localhost','Sensores','Ultra_sonico',27017)
                db = mongo.Ultra_sonico
                collection = db.Sensores
                collection.find().pretty()
                
                for col in collection:
                    print("_____")
                    print("Movimiento: ", )
                    print("Fecha: ", )
                    print("_____\n")
                print("Resultado MONGODB")
                print()
                #CONSULTA EN MONGO

                #CONSULTA EN ARCHIVO
                #ROSA
                print("Resultado Archivo")
                print()
                #CONSULTA EN ARCHIVO
            elif opcion == "4":
                ciclo2 = False

    elif opcion == "4":
        print("bye...")
        ciclo = False

