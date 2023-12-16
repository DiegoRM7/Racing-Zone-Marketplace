from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module

EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "racing-zone_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone_number = data.get('phone_number', None)
        self.password = data.get('password', None)
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cars = []

    @staticmethod
    def flash_msg_must_login():
        flash("You don't have a current session open. You must register as a new user or login with an existing account!","no_session")

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for one_user in results:
            users.append(cls(one_user))
        return users

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {"id": id})
        return cls(results[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        # if didn't find matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email, phone_number, password, created_at, updated_at)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone_number)s, %(password)s, NOW(), NOW());
            """
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_user(user_form):
        is_valid = True         # we assume this is true
        if len(user_form['first_name']) < 2:
            flash("First name must be at least 2 characters.",'register')
            is_valid = False
        if len(user_form['last_name']) < 2:
            flash("Last name must be at least 2 characters.",'register')
            is_valid = False
        if not EMAIL_REGEX.match(user_form['email']):
            flash("Invalid email address! Must use proper formatting.",'register')
            is_valid = False
        for user in User.get_all():
            if user.email == user_form['email']:
                flash("Email already exists in database!",'register')
                is_valid = False
        if len(user_form['phone_number']) < 10:
            flash("Phone number must be at least 10 numbers.",'register')
            is_valid = False
        if len(user_form['password']) < 8:
            flash("Password must be at least 8 characters.",'register')
            is_valid = False
        if user_form['confirm_password'] != user_form['password']:
            flash("Confirmed password must match password.",'register')
            is_valid = False
        return is_valid