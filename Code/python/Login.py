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

index=int(input("Tiene cuenta?\n1 -Si\n2 -No\nInput(1 - 2): "))

if index==1:        #login
    username=input("Ingrese su nombre de usuario: ")
  
if index==2:        #registro
  # Comprueba validez
  while True:
    username=input("Ingrese su nombre de usuario: ")
    if vf.char_verify("username",username) and vf.verify("username",username):
        break
  
  while True:
    mail=input("Ingrese su correo electronico: ")
    if vf.char_verify("mail",mail) and vf.verify("mail",mail):
       break
  while True:
    password=input("Ingrese su contraseña: ")
    password2=input("Vuelva a ingresar su contraseña: ")
    if password==password2:
       break
    else:
      print("Las contraseñas no coinciden")
  
  cursor.execute(
    "INSERT INTO users (username, mail, password) VALUE (%s , %s , %s);",
    (username, mail, password)
    )
  mydb.commit()