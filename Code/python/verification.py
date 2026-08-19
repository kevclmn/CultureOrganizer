import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="102104",
  database="culture_organizer",
)

cursor=mydb.cursor()


# Verificacion de existencia en base de datos
def verify(column,parameter):
  cursor.execute(
  "SELECT COUNT(*) FROM users WHERE "+ column +" = %s LIMIT 1;",
  (parameter,)
  )
  if cursor.fetchone()[0]==0:
     return True
  else:
    return False


# Verificacion de caracteres 
mailchar=("1234567890QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm.@")
userchar=("1234567890QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm._")

def char_verify(input_type ,user_input):
  #
  match input_type:
    case "mail":
        acount=0
        dotcount=0
        for character in user_input:
          if character not in mailchar:
            st.error("Caracteres invalidos")
            return False 
          if "@" == character:      #REVISAR METODO DE FILTRADO XD
            acount=acount+1
          if "." == character:
            dotcount=dotcount+1
        if dotcount > 1 or acount > 1 or dotcount==0 or acount == 0:
          st.error("Revisa los puntos y los arrobas")
          return False
        return True
    case "username":
            for character in user_input:
              if character not in userchar:
                st.error("Caracteres invalidos")
                return False 
            return True