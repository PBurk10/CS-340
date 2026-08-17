# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 
import urllib.parse


class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'p@ssword' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        client = MongoClient('mongodb://user:p%40ssword@localhost:27017/?authSource=admin') 
        self.database = self.client[DB] 
        self.collection = self.database[COL] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            self.collection.insert_one(data)  # data should be dictionary 
            return True
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, criteria=None):
        if criteria is not None:
            cursor = self.collection.find(criteria)
            
        else:
            cursor = self.collection.find({})
            
        return list(cursor)
    
     #Update
    def updateRecord(self, query, newValue):
        if not query:
            raise Exception("No search query.")
        elif not newValue:
            raise Exception("No updated value is present.")
        else:
            _updateValid = self.dataBase.animals.update_many(query, {"$set": newValue})
            self.records_updated = _updateValid.modified_count
            self.records_matched = _updateValid.matched_count
            
            return True if _updateValid.modified_count > 0 else False
    
    #Delete
    def deleteRecord(self, query): 
        if not query:
            raise Exception("No search criteria present.")
            
        else:
            _deleteValid = self.dataBase.animals.delete_many(query)
            self.records_deleted = _deleteValid.deleted_count
            
            return True if _deletedValid.deleted_count > 0 else False