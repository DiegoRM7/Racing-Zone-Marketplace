from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Car:
    DB = "racing-zone_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.year = data['year']
        self.make = data['make']
        self.model = data['model']
        self.transmission = data['transmission']
        self.horsepower = data['horsepower']
        self.weight = data['weight']
        self.image_path = data.get('image_path', None)
        self.price = data['price']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO cars (user_id, year, make, model, transmission, horsepower, weight, image_path, price, title, description)
                VALUES (%(user_id)s, %(year)s, %(make)s, %(model)s, %(transmission)s, %(horsepower)s, %(weight)s, %(image_path)s,
                        %(price)s, %(title)s, %(description)s);
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def all_users_all_cars(cls):
        query = """
                SELECT *
                FROM cars
                JOIN users
                ON cars.user_id = users.id;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        all_cars = []
        for row in results:
            car = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "phone_number": row["phone_number"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            car.creator = User(user_data)
            all_cars.append(car)
        print(f"These are all the car objects:\n{all_cars}")
        return all_cars

    # @classmethod
    # def update(cls, data):
    #     query = """
    #             UPDATE pies SET name = %(name)s, filling = %(filling)s, crust = %(crust)s, id = %(id)s, user_id = %(user_id)s
    #             WHERE id = %(id)s;
    #         """
    #     results = connectToMySQL(cls.DB).query_db(query, data)
    #     print(results)
    #     return results
    

    # @staticmethod
    # def validate_pie(pie_form):
    #     is_valid = True
    #     if len(pie_form['name']) < 1:
    #         flash("Must enter a name.",'create_pie')
    #         is_valid = False
    #     if len(pie_form['filling']) < 1:
    #         flash("Must enter the filling of the pie.",'create_pie')
    #         is_valid = False
    #     if len(pie_form['crust']) < 1:
    #         flash("Must enter a crust for the pie.",'create_pie')
    #         is_valid = False
    #     for one_pie in Pie.get_all():
    #         if str(pie_form['name']) == 'current_pie_name':
    #             print(f"\n\nError same name and not updating and validation\n\n")
    #             break
    #         elif str(pie_form['name']) == one_pie.name:
    #             flash("Error! Name already exists for pie. Create a different name.",'create_pie')
    #             is_valid = False
    #     return is_valid

    # @staticmethod
    # def validate_pie_deletion_through_url(id):
    #     is_valid = True
    #     for one_pie in Pie.get_all():
    #         if 'int_registered_user' != one_pie.user_id:
    #             is_valid = False
    #     return is_valid

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM pies;"
    #     results = connectToMySQL(cls.DB).query_db(query)
    #     all_pies = []
    #     for one_pie in results:
    #         all_pies.append(cls(one_pie))
    #     return all_pies

    # @classmethod                           
    # def get_one_pie_by_id_w_user(cls, id):      
    #     query = """
    #             SELECT * FROM pies JOIN users
    #             ON pies.user_id = users.id WHERE pies.id = %(id)s;
    #             """
    #     results = connectToMySQL(cls.DB).query_db(query, {"id": id})
    #     print(results[0])
    #     pie = cls(results[0])
    #     user_data = {
    #         "id":["users.id"],
    #         "first_name":["first_name"],
    #         "last_name":["last_name"],
    #         "email":["email"],
    #         "created_at":["users.created_at"],
    #         "updated_at":["users.updated_at"]
    #         }
    #     pie.creator = User(user_data)
    #     return pie
    
    # @classmethod
    # def delete(cls, id):
    #     query = """
    #             DELETE FROM pies
    #             WHERE id = %(id)s;
    #             """
    #     return connectToMySQL(cls.DB).query_db(query, {"id":id})
    
    # @classmethod
    # def get_pies_of_one_user(cls, id):
    #     query = """
    #             SELECT * FROM pies JOIN users
    #             ON pies.user_id = users.id
    #             WHERE users.id = %(id)s;
    #             """
    #     results = connectToMySQL(cls.DB).query_db(query, {"id": id})
    #     all_pies_from_one_user = []
    #     for row in results:
    #         pie = cls(row)
    #         user_data = {
    #             "id":row["users.id"],
    #             "first_name":row["first_name"],
    #             "last_name":row["last_name"],
    #             "email":row["email"],
    #             "password":row["password"],
    #             "created_at":row["users.created_at"],
    #             "updated_at":row["users.updated_at"]
    #             }
    #         pie.creator = User(user_data)
    #         all_pies_from_one_user.append(pie)
    #     print(f"These are all the pie objects:\n{all_pies_from_one_user}")
    #     return all_pies_from_one_user