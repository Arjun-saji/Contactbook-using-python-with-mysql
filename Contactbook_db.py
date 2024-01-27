import mysql.connector
try:
   # Connect to the MySQL server
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="Root@123"
    )

   # Create a cursor object
   mycursor = mydb.cursor()

   # Execute the SQL statement to create the database
   mycursor.execute("CREATE DATABASE Dbcontactbook")

   # Print a success message
   print("Database created sucessfully")
     # to create a new table
   # Connect to the MySQL server
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="Root@123",
   database = 'Dbcontactbook'
    )
   # Create a cursor object
   mycursor = mydb.cursor()
   mycursor.execute("CREATE TABLE ContactList(name varchar(50),phoneNumber bigint)")
   print("Table Created succesfully..!")
except:
   print("Its Already Exists")

 # to insert data in table
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Root@123",
database = 'Dbcontactbook'

)

   # Create a cursor object
mycursor = mydb.cursor() 
# # Close the cursor and database connection
   # mycursor.close()
   # mydb.close()
while True :
   print("Menu")
   print("1.Insertion\n 2.Updation\n 3.Deletion\n 4.Display\n 5.Exit")
   chce=int(input("Enter your Choice :"))
   if chce ==1:
     print("Insert new contact")
     name = input("Enter the Name to insert: ")
     phoneNumber = int(input("Enter the phone number to insert: "))
     mycursor.execute("SELECT *FROM ContactList")
     list1 = mycursor.fetchall()
     flag = 0
     for i in list1:
       if i[0] == name:
         print("Contact already Exists")
         flag = 1
     if flag ==0: 
          mycursor.execute("INSERT INTO ContactList(name,phoneNumber) VALUES (%s,%s)",(name,phoneNumber))
          print("Contact Added succesfully..!")
          mydb.commit() 
   elif chce==2:
       print("1.Name updation\n 2. Phonenumber updation")
       update= int(input("Enter Updation choices :"))
       if update==1:
          old=input("Enter the old name :")
          new=input("Enter the new name: ")
          mycursor.execute("SELECT name FROM ContactList")
          list2=mycursor.fetchall()
          flag=0
          for i in list2:
             if i[0] == new:
                print("Contact exists")
                flag=1
          if flag==0 :
                mycursor.execute("UPDATE ContactList SET name = %s WHERE name = %s",(new,old))
                print("Contact updated succesfully..!")
                mydb.commit()
       else:
          name=input("Enter the Name:")
          phoneNumber=int(input("Enter the new phone number: "))
          mycursor.execute("UPDATE ContactList SET phoneNumber = %s WHERE name = %s",(phoneNumber,name))
          print("phone Number updated succesfully..!")
          mydb.commit()
   elif  chce==3:
       print("contact Deletion")
       name=input("Enter the Name to Delete: ")
       mycursor.execute("DELETE FROM ContactList WHERE name = %s",(name,))
       print("Contact Deleted..!")
       mydb.commit()
   elif chce==4:
       mycursor.execute("SELECT *FROM ContactList")
       list3=mycursor.fetchall()
       for i in list3:
          print(i) 
   else:
       exit()         










      


        



 



  



 
