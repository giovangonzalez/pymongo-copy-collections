import hashlib
from decimal import Decimal
import time
from pymongo import MongoClient

# connect to both engines
MongoClientSource = MongoClient('mongodb://connectionString1') # change this. this is using a standard connection string format
MongoClientTarget = MongoClient('mongodb+srv://connectionString2') # change this. this is using a new connection string format

# set both databases
MongoDbSource=MongoClientSource.database_name # change this to your database name
MongoDBTarget=MongoClientTarget.database_name # change this to your database name

#start copy
for collection in MongoDbSource.collection_names():
  print('collection ' + str(collection))
  # delete all existing documents in current collection on target database
  MongoDBTarget[collection].delete_many({})
  documents = 0 # this is just a counter
  # get all source documents from current collection
  for document in MongoDbSource[collection].find({}):
    # insert document into target collection
    documentId = MongoDBTarget[collection].insert_one(document).inserted_id
    documents += 1
  print('\t'+ str(collection) + ' migrated: '+ str(documents))
