import firebase_admin
from firebase_admin import credentials , firestore

#Provide authentication for entering the Firestore database.

cred = credentials.Certificate("accountkey.json.json")
firebase_admin.initialize_app(cred)

# Connect to our firestore database then open up one of the collections inside. 

db = firestore.client()  # this connects to our Firestore database
collection = db.collection('players')  # opens 'players' collection
doc = collection.document('jcarlson')  # specifies the 'jcarlson' document

# GET for certain documents in the collection. Acts sort of like a select statement.
#doc = collection.document('jcarlson')
#res = doc.get().to_dict()
#print(res)

# Print the documents within our collection
#docs = collection.get()
#print(docs)

# create documents within our collection.

#res = collection.document('scarlson').set({
    #'faction': 'sepertatists',
    #'firstname': 'silas',
    #'lastname': 'carlson'
#})
#print(res)

# Ability to modify our documents that are currently in our database.
#res = collection.document('scarlson').update({
    #'faction': 'republic'
#})


# Code to delete an entire document inside of a collection
#collection.document('scarlson').delete()

# Code to delete a single field within a document.
#collection.document('scarlson').update({
    #'faction': firestore.DELETE_FIELD})

# To write queries we use the where method. the structure is where(fieldpath,opStr,value)
res = collection.where('faction', '==', 'empire').get()
print(res)

