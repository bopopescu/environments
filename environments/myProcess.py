import storage

mydb = storage.connect()

print(mydb)

if mydb.is_connected():
    db_Info = mydb.get_server_info()
    print("Connected to MySQL database... MySQL Server version on ", db_Info)
    mycursor = mydb.cursor()
    mycursor.execute("select * from serverInfo")
    myresult = mycursor.fetchall()
    for x in myresult:
        print ("Your Rows Here - ", x)