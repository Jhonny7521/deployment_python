from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from datetime import datetime

class Show:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.like = data['like']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.users_like = []

    @classmethod
    def save_show(cls, formulario):
        
        query = "INSERT INTO shows (title, network, release_date, description, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);"
        new_show_id = connectToMySQL('belt_python').query_db(query, formulario)
        return new_show_id

    @staticmethod
    def valida_show(formulario):
        
        es_valido = True
        print('----')
        print(datetime.today())
        print('----')
        
        if len(formulario['title']) < 3:
            flash('El título debe ser de almenos 3 caracteres','show')
            es_valido = False

        if len(formulario['network']) < 3:
            flash('La red debe ser de almenos 3 caracteres','show')
            es_valido = False

        #Validar que la fecha no este vacia
        if formulario['release_date'] != '':
            
            if datetime.strptime(formulario['release_date'], '%Y-%m-%d') < datetime.today():
                flash('La fecha debe ser posterior al dia de hoy','show')
                es_valido = False
        else:
            flash('Ingrese una fecha','show')
            es_valido = False
        
        #vaidamos si el estado es sean mayor a 3 caracteres
        if len(formulario['description']) < 3:
            flash('La descripción debe ser de almenos 3 caracteres','show')
            es_valido = False
        
        return es_valido
    
    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows ORDER BY title ASC"
        results = connectToMySQL('belt_python').query_db(query)
        print(results)
        shows = []
        for r in results:
            shows.append(cls(r))
        return shows

    @classmethod
    def get_all_shows_of_user(cls, data):
        query = "SELECT * FROM shows WHERE user_id = %(id)s;"
        results = connectToMySQL('belt_python').query_db(query, data)
        print(results)
        shows = []
        for r in results:
            shows.append(cls(r))
        return shows

    @classmethod
    def get_by_id(cls, data):
        
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        result = connectToMySQL('belt_python').query_db(query, data)
        print (data)
        if len(result) < 1:
            return False
        else :
            shw = result[0]
            show = cls(shw)
            return show

    @classmethod
    def update_show(cls, formulario):
        query = "UPDATE shows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s, description=%(description)s WHERE id = %(id)s;"
        results = connectToMySQL('belt_python').query_db(query, formulario)
        return results

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM shows WHERE id = %(id)s'
        return connectToMySQL('belt_python').query_db(query, data)

    @classmethod
    def like_show_save(cls, data):      

      query = "INSERT INTO users_has_shows (user_id, show_id) VALUES (%(user_id)s, %(show_id)s);"
      like_show = connectToMySQL('belt_python').query_db(query, data)
      return like_show 

    @classmethod
    def find_if_like_show(cls, data):      

      # query = "SELECT * FROM shows WHERE id = %(id)s;"
      # query = "SELECT * FROM users LEFT JOIN users_has_shows ON users.id = user_id LEFT JOIN shows ON shows.id = show_id WHERE users.id = %(id)s"
      query = "SELECT first_name FROM users LEFT JOIN users_has_shows ON users.id = user_id LEFT JOIN shows ON shows.id = show_id WHERE users.id = %(id)s;"
      result = connectToMySQL('belt_python').query_db(query, data)
      print (result)
      if len(result) < 1:
          return False
      else :
          return True

    
    @classmethod
    def update_show_like(cls, data2):
        query = "UPDATE shows SET like=%(like)s WHERE id = %(id)s;"
        results = connectToMySQL('belt_python').query_db(query, data2)
        return results

