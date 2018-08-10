import pymongo
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
uprompt = ""

print("Running Banana Farm v1.0.0")
print("Type 'help' for a List of Commands.")
uprompt = input("")

if uprompt == "help":
    print("dbcreate - creates a database.")
    print("version - prints the version number to the screen.")
    print("checkdb - checks the databases on the host.")

elif uprompt == "checkdb":
    print(client.list_database_names())

elif uprompt == "dbcreate":
    dbname = input("Please input the Database name: ")
    db = client[dbname]
    colname = input("Please input a new collection name: ")
    col = db[colname]
    ndict = { "x": "x", "x": "x" }
    x = col.insert_one(ndict)
    print(x)

    
    


    
