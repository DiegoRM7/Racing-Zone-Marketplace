from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash, session, request

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
        self.image_path = data['image_path']
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
        return all_cars

    @classmethod
    def update(cls, data):
        query = """
                UPDATE cars
                SET year = %(year)s, make = %(make)s, model = %(model)s, transmission = %(transmission)s, horsepower = %(horsepower)s,
                weight = %(weight)s, image_path = %(image_path)s, price = %(price)s, title = %(title)s, description = %(description)s
                WHERE id = %(id)s;
            """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results

    @staticmethod
    def validate_car_listing(car_form):
        is_valid = True
        # for price
        if len(car_form['price']) < 1:
            flash("Must enter a price",'create_car_listing(listing_details)')
            is_valid = False
        if len(car_form['price']) < 5:
            flash("Price must be at least 10,000",'create_car_listing(listing_details)')
            is_valid = False
        # for title
        if len(car_form['title']) < 1:
            flash("Must enter a title for the listing",'create_car_listing(listing_details)')
            is_valid = False
        for one_car in Car.get_all():
            # checking to see if I have a current session of current car when updating a car and if i do then skip that title check, let it pass.
            # if its a new entry listing then the session won't exist so it will still be looking for all car titles.
            if str(car_form['title']) == one_car.title:
                if str(car_form['title']) == session['current_car_title']: continue
                print(f"\n\nError same name and not updating and validation\n\n")
                flash("Title already exists in current listings. Write a different title",'create_car_listing(listing_details)')
                is_valid = False
        # for image_path file/string/varchar
        # ???? SOMETHING IS WRONG WITH THIS VALIDATION ON CHECKING IF THE FILE EXISTS OR NOT.
        # ?? ITS SAYING IT ALWAYS DOESN'T EVEN WHEN A FILE IS SUBMITTED
        # if request.files(file) == "...":
        #     flash("Must upload an image file.",'create_car_listing(no_image)')
        #     is_valid = False
        # for description
        if len(car_form['description']) < 1:
            flash("Must enter a description for the listing",'create_car_listing(listing_details)')
            is_valid = False
        # for year
        if len(car_form['year']) < 1:
            flash("Must enter the year production of the car",'create_car_listing(car_details)')
            is_valid = False
        # for make
        if len(car_form['make']) < 1:
            flash("Must enter a make brand for the car",'create_car_listing(car_details)')
            is_valid = False
        # for model
        if len(car_form['model']) < 1:
            flash("Must enter a model for the car",'create_car_listing(car_details)')
            is_valid = False
        # for transmission
        if len(car_form['transmission']) < 1:
            flash("Must enter a transmission type for the car, either Automatic or Manual",'create_car_listing(car_details)')
            is_valid = False
        # for horsepower
        if len(car_form['horsepower']) < 1:
            flash("Must enter the horsepower the car possesses",'create_car_listing(car_details)')
            is_valid = False
        # for weight
        if len(car_form['weight']) < 1:
            flash("Must enter the weight of the car in LBS",'create_car_listing(car_details)')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_car_deletion_through_url(id):
        is_valid = True
        car = Car.get_one_car_by_id_w_user(id)
        if (session['int_registered_user']) != car.user_id:
            is_valid = False
        return is_valid
    
    @classmethod
    def purchase_car_listing(cls, data):
        query = """
                UPDATE cars 
                SET user_id = %(id_of_buyer)s 
                WHERE id = %(id_of_car_being_bought)s;
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    # later on will make a static method/function here/under to change the amount
    # of credits of the user lower/or higher based on when they purchase a listing, 
    # sell one, or delete one (return back to broker for stock price).
        # @staticmethod
        # def alter_user_credits(id_of_user):
        #   return user_credits

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_cars = []
        for one_car in results:
            all_cars.append(cls(one_car))
        return all_cars

    @classmethod
    def get_one_car_by_id_w_user(cls, id):
        query = """
                SELECT * FROM cars JOIN users
                ON cars.user_id = users.id WHERE cars.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, {"id": id})
        car = cls(results[0])
        user_data = {
            "id":["users.id"],
            "first_name":["first_name"],
            "last_name":["last_name"],
            "email":["email"],
            "phone_number":["phone_number"],
            "created_at":["users.created_at"],
            "updated_at":["users.updated_at"]
            }
        car.creator = User(user_data)
        return car
    
    @classmethod
    def delete(cls, id):
        query = """
                DELETE FROM cars
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query, {"id":id})
    
    @classmethod
    def get_all_cars_one_user(cls, id):
        query = """
                SELECT * FROM cars JOIN users
                ON cars.user_id = users.id
                WHERE users.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, {"id": id})
        all_cars_from_one_user = []
        for row in results:
            car = cls(row)
            user_data = {
                "id":row["users.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "phone_number":row["phone_number"],
                "password":row["password"],
                "created_at":row["users.created_at"],
                "updated_at":row["users.updated_at"]
                }
            car.creator = User(user_data)
            all_cars_from_one_user.append(car)
        print(f"These are all the car listing objects in this user's garage:\n{all_cars_from_one_user}")
        return all_cars_from_one_user