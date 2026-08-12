# Registro / Login de usuarios
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="102104"
)
index=input("Tiene cuenta?\n1 -Si\n2 -No\nInput(1 - 2): ")

if index==1:        #login
  username=input("Ingrese su nombre de usuario: ")


if index==2:        #registro
  username=input("Ingrese su nombre de usuario: ")