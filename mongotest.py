from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Example: Insert a document
document = {'name': 'John', 'age': 30}
collection.insert_one(document)

# Example: Query documents
for doc in collection.find():
    print(doc)