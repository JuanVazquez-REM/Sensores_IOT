import pymongo
from pymongo import database

class Database2:


    def __init__(client, col,db):
        client = pymongo.MongoClient('localhost')
        db = client[db]
        col = db[col]


    def select_one(self): #uno simple       
        doc = self.col.find_one({}).pretty()
        return doc

    def ultimoDato(self): #ultimoDato
        doc = self.col.find_one({"$query":{}, "$orderby":{"$natural":-1}})
        return doc

    def varios(self): #varios
        resultados = self.col.find({}).pretty()
        return resultados

    def insertar(self, data): #insertar
        self.col.insert_one(data)