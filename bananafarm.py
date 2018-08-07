import pymongo

myclient = pymongo.MongoClient(HOSTNAME_HERE)

print("Running Banana Farm v1.0.0")
print("Type 'help' for a List of Commands.")
uprompt = input("")

if uprompt == "help":
    print("dbcreate - creates a database.")
    print("version - prints the version number to the screen.")
    print("checkdb - 


    
