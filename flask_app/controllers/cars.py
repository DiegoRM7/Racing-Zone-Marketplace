from flask_app import app
from flask import render_template, redirect, request, session, flash, send_from_directory
from flask_app.models.car import Car
from flask_app.models.user import User
from werkzeug.utils import secure_filename
import os

@app.route('/home')
def home_page_all_listings():
    if 'int_registered_user' not in session:
        User.flash_msg_must_login()
        return redirect('/login')
    
    # putting in the files from the directory /images into the home page as an array
    image_files = os.listdir('flask_app/static/images/')
    print(image_files)
    print(image_files[0])
    
    user = User.get_by_id(session['int_registered_user'])
    session['signed_in_user_name'] = user.first_name + ' ' + user.last_name
    return render_template("home.html", cars = Car.all_users_all_cars(), image_files = image_files)

@app.route('/account_and_garage')
def account_and_garage_details():
    if 'int_registered_user' not in session:
        User.flash_msg_must_login()
        return redirect('/login')
    
    image_files = os.listdir('flask_app/static/images/')
    all_cars_of_user = Car.get_all_cars_one_user(session['int_registered_user'])
    car_counter = 0
    for i in all_cars_of_user:
        car_counter += 1
    return render_template("account_and_garage.html", all_cars_of_user = all_cars_of_user, car_counter = car_counter, image_files = image_files)

@app.route('/listing/create')
def create_listing_page():
    if 'int_registered_user' not in session:
        User.flash_msg_must_login()
        return redirect('/login')
    if session.get('current_car_title') != None:
        session.pop('current_car_title')
    return render_template("create_listing.html")

@app.route('/listing/create/process', methods=["POST"])
def create_listing_process():
    file = request.files['image_file']
    print(file)
    
    if not Car.validate_car_listing(request.form):
        print("---Car listing could not be created.----\n----Validation gone wrong!----")
        if not file:
            flash("Must upload an image file.",'create_car_listing(no_image)')
        return redirect('/listing/create')
    
    # ? Uploading to the static/images folder as a file with the name being the image_path name.
    if file:
        for i in file.filename:
            if i == " ":
                flash("Car listing could not be created.\nMust enter a file name with correct syntax: replaces spaces with underscores '_'",'correct_file_name')
                return redirect('/listing/create')
            
        file.save(os.path.join('flask_app/static/images/', (file.filename)))
        print('image was saved in static/images folder!')

    Car.save(request.form)
    print("Car was created!!!!!!!!")
    return redirect('/home')

@app.route('/listing/view/<int:id>')
def show_one(id):
    if 'int_registered_user' not in session:
        User.flash_msg_must_login()
        return redirect('/login')
    
    image_files = os.listdir('flask_app/static/images/')
    return render_template('view_listing.html', cars = Car.get_one_car_by_id_w_user(id), image_files = image_files)

@app.route('/listing/purchase', methods=["POST"])
def purchase_process():
    Car.purchase_car_listing(request.form)
    print("Car was purchased for $$$$ !!")
    # another method here that will change the credits of buyer once the transaction/transfer is done.
    return redirect('/account_and_garage')

@app.route('/listing/edit/<int:id>')
def edit_listing_page(id):
    if 'int_registered_user' not in session:
        User.flash_msg_must_login()
        return redirect('/login')
    
    image_files = os.listdir('flask_app/static/images/')
    car = Car.get_one_car_by_id_w_user(id)
    session['current_car_title'] = car.title
    return render_template('edit_listing.html', car = car, image_files = image_files)

@app.route('/listing/edit/process', methods=["POST"])
def update_car():
    if not Car.validate_car_listing(request.form):
        print("---Car listing could not be updated.----\n----Validation gone wrong!----")
        return redirect(f"/listing/edit/{request.form['id']}")
    
    file = request.files['image_file']
    if file:
        for i in file.filename:
            if i == " ":
                flash("Car listing could not be created.\nMust enter a file name with correct syntax: replaces spaces with underscores '_'",'correct_file_name')
                return redirect(f"/listing/edit/{request.form['id']}")
            
        file.save(os.path.join('flask_app/static/images/', (file.filename)))
        print('image was saved in static/images folder!')

    Car.update(request.form)
    print("------------CAR LISTING UPDATED SUCCESSFULLY!-------------")
    return redirect('/account_and_garage')

@app.route('/listing/delete/<int:id>')
def delete(id):
    if not Car.validate_car_deletion_through_url(id):
        print(f"\n\nError! Can't delete car listing, its not from your account!!!!!\n\n")   #! later set up to a flash or modal
        return redirect(f"/account_and_garage")
    
    Car.delete(id)
    print(f"\n\nDeleted the listing from your account! It is not listed on the home page anymore!\n\n")  #! later set up to a flash or modal
    return redirect('/account_and_garage')

@app.route('/serve_image/<filename>')
def serve_image(filename):
    return send_from_directory('static/images/', filename)