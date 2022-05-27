#todo lo que tiene que ver con la base de datos de usuarios
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re #importamos las expresiones regulares para validaciones de contraseñas
#definimos la expresion regular para validar la contraseña
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #se coloca fuera de la clase xq no tiene que ver con ella

from flask import flash

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.shows_like = []
    
    #Funcion para guardar usuario
    @classmethod
    def save(cls, formulario):
        # formulario = {
        # "first_name":  "Elena",
        # "last_name":  De Troya,
        # "email":  elena@cd.com,
        # "password": HSds546sdWEeSDFD6a445 #contraseña encriptada
        # }

        #si el query es select recibimos un diccionarion con todos los datos que consultamos
        #si el query es insert solo recibimos el id de la fila nueva insertada

        query = "INSERT INTO users(first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        nuevoId = connectToMySQL('belt_python').query_db(query, formulario)
        return nuevoId

    @staticmethod
    def valida_usuario(user):
        #El user tiene una forma similar a esta
        # user = {
        #     "first_name": "Emilia",
        #     "last_name": "Mendoza",
        #     "email": "emilia@codingdojo.com",
        #     "password": 123456
        # }
        #variable para ver si algun dato esta incorrecto
        es_valido = True

        #validamos los datos recibidos esten correctos
        if len(user['first_name']) < 3:
            flash('Nombre debe ser de almenos 3 caracteres', 'register')
            es_valido = False

        #Validar que el apellido sea amayor a dos caracteres
        if len(user['last_name']) < 3:
            flash('Apellido debe de tener almenos 3 caracteres', 'register')
            es_valido = False
        #vaidamos si la estructura del correo es correcto
        if not EMAIL_REGEX.match(user['email']):#aqui verificamos si la contraseña cumple con la expresion regular
            flash('E-mail invalido', 'register') #si tiene los caracteres admitidos
            es_valido = False
        
        #Validar que la contraseña sea mayor a 6 caracteres
        if len(user['password']) < 8 :
            flash('Contraseña debe de ser de almenos 8 caracteres', 'register')# register = (category_filter = ['register']) --> en html
            es_valido = False

        if user['password'] != user['confirm'] :
            flash('Contraseñas no coinciden', 'register')
            es_valido = False

        #Validamos si ya existe un correo electronico con ese email
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('belt_python').query_db(query, user)
        if len(results) >= 1:
            flash('E-mail ya registrado previamente', 'register')
            es_valido = False
        
        return es_valido

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('belt_python').query_db(query, data)
        usr = results[0]#tomo el dato de la posicion 0 de result
        user = cls(usr)#lo convierto en un objeto de la clase User 
        #ahora tendra todos los atributos de id, first_name, last_name , etc lo que se declaro al inicio
        #y regreso el objeto user
        return user
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('belt_python').query_db(query, data)

        if len(results) < 1 :

            return False
        else:
            usr = results[0]#tomo el dato de la posicion 0 de result
            user = cls(usr)#lo convierto en un objeto de la clase User 
            #ahora tendra todos los atributos de id, first_name, last_name , etc lo que se declaro al inicio
            #y regreso el objeto user
            return user


