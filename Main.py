from Sensores import Sensores
from Mongo import Database2
from Mysql import Mysql
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
            print("------------Menu Sensor------------")
            print("1-Calcular Tempratura y humedad")
            print("2-Mostrar ultimo dato registrado")
            print("3-Mostrar todos los datos registrados")
            print("------------")
            opcion = input("Elije una opcion: ")
            
            if opcion == "1":
                #CALCULANDO TEMPERATURA Y HUMEDAD
                Sensor = Sensores()
                data = Sensor.Get_Temperatura_Humedad(15,"DHT11")
                resultado = Sensor.Get_Temperatura_Humedad(13,"DHT22")
                print("Calculando Temperatura y Humedad...")
                print(data)
                #CALCULANDO TEMPERATURA Y HUMEDAD

                #GUARDANDO DATOS EN MYSQL
                mysql = Mysql('localhost','administrador','admin','sensores_python')
                sql = 'INSERT INTO temperatura_humedad (temperatura, humedad) VALUES ('+ data.temperatura +', '+ data.humedad +');'
                mysql.insert(sql)
                mysql.close()
                #GUARDANDO DATOS EN MYSQL
                print("Guardando datos en...")
                print("Mysql...")
                #aqui para mongo
                mongo = Database2('localhost','Sensores','Temperatura_Humedad')
                mongo2 = 'db.Sensores.insert '+ (data.temperatura + ',' + data.humedad)
                mongo.insert(mongo2)
                mongo.close()
                print("Guardando datos en Mongo")

            elif opcion == "2":
                sql = 'SELECT * FROM sensores_python.temperatura_humedad order by id DESC LIMIT 1'
                #CONSULTA EN MYSQL
                resultado = Mysql('localhost','administrador','admin','sensores_python')
                dato = resultado.select_one(sql)
                print()
                print("Id: ", dato[0])
                print("Temperatura: ", dato[1])
                print("Humedad: ", dato[2])
                print("Guardando datos en MySql")

                mongo = Database2('localhost','Sensores','Temperatura_Humedad')
                mongo2 = 'db.Sensores.insert '+ (data.temperatura + ',' + data.humedad)
                mongo.insert(mongo2)
                print()
                print("Id: ", dato[0])
                print("Temperatura: ", dato[1])
                print("Humedad: ", dato[2])
                print("Guardando datos en Mongo")
            
            elif opcion == "3":
                sql = 'SELECT * FROM temperatura_humedad'
                #CONSULTA EN MYSQL
                query = Mysql('localhost','administrador','admin','sensores_python')
                resultados = query.select(sql)
                print("---Datos---")
                for columna in resultados:
                    print("_____")
                    print("Id: ", columna[0])
                    print("Temperatura: ", columna[1])
                    print("Humedad: ", columna[2])
                    print("_____\n")
                query.close()
                #CONSULTA EN MYSQL
                mg = 'db.find({}).pretty()'
                mongo = Database2('localhost','Sensores','Temperatura_Humedad')
                mongo2 = 'db.find'({ + dato.temperatura + ','+ dato.humedad })
                resultadosM = mongo2.select(mg)
                for col in resultadosM:
                    print("_____")
                    print("Id: ", columna[0])
                    print("Temperatura: ", columna[1])
                    print("Humedad: ", columna[2])
                    print("_____\n")
                mongo.close()
        print("opcion 1")

    elif opcion == "2":
        print("opcion 2")

    elif opcion == "3":
        print("opcion 3")

    elif opcion == "4":
        print("bye...")
        ciclo = False

