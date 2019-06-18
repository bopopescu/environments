import mysql.connector
from mysql.connector import Error ##error when we failed to connect 


try:
    mydb = mysql.connector.connect(
                                   host="localhost",
                                   user="root",
                                   passwd="manish@12345",
                                   database="test"
                                   )
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        mycursor = mydb.cursor()
        mycursor.execute("select * from serverInfo")
        myresult = mycursor.fetchall()
        for x in myresult:
            print ("Your Rows Here - ", x)
        #cursor.close()   #print("I am a good person")
except Error as e:
    print ("Error while connecting to MySQL", e)



