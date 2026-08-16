# Registro / Login de usuarios
import mysql.connector
import verification as vf

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="102104",
  database="culture_organizer",
)

cursor=mydb.cursor()


username=input("Ingrese su nombre de usuario: ")
mail=input("Ingrese su email: ")

user_verify= vf.verify("username",username)
mail_verify= vf.verify("mail", mail)
if user_verify==1 or mail_verify==1 :
    if user_verify==1:
        print("Ese nombre de usuario ya existe\n")
    if mail_verify == 1:
        print("Ese correo electronico ya está vinculado")
    
if user_verify==0 and mail_verify==0 :
    cursor.execute(
    "INSERT INTO users (username) VALUE (%s);",
    [username]
    )
    mydb.commit()
    print("Usuaro registrado")
