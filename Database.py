from gridfs import Database
from pymongo import MongoClient

class Database:
    def __init__(self, DatabaseVar, CollectionVar):
        Mongo = MongoClient('mongodb://localhost:27017/')
        self.MyDatabase = Mongo[DatabaseVar]
        self.MyCollection = self.MyDatabase[CollectionVar]