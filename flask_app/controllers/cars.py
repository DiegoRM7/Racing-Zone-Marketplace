from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.car import Car
from flask_app.models.user import User

@app.route('/home')
def home_page_all_listings():
    if 'int_registered_user' not in session:
        User.flash_msg_must_login()
        return redirect('/login')
    user = User.get_by_id(session['int_registered_user'])
    session['signed_in_user_name'] = user.first_name + ' ' + user.last_name
    return render_template("home.html", cars = Car.all_users_all_cars())

@app.route('/account_and_garage')
def account_and_garage_details():
    if 'int_registered_user' not in session:
        User.flash_msg_must_login()
        return redirect('/login')
    all_cars_of_user = Car.get_all_cars_one_user(session['int_registered_user'])
    car_counter = 0
    # loop through the data of cars
    for i in all_cars_of_user:
        car_counter += 1
    print(car_counter)
    return render_template("account_and_garage.html", all_cars_of_user = all_cars_of_user, car_counter = car_counter)

@app.route('/listing/create')
def create_listing_page():
    return render_template("create_listing.html")

@app.route('/listing/create/process', methods=["POST"])
def create_listing_process():
    # if not Car.validate_pie(request.form):    # ? later on create a validation of all the fields (there's a lot to validate)
    #     print("---Car could not be created.----\n----Validation gone wrong!----")
    #     return redirect('/dashboard')
    Car.save(request.form)
    print("Car was created!!!!!!!!")
    return redirect('/home')

# ? copy of the previous dashboard taking bits and pieces from.
# @app.route('/dashboard')
# def dashboard_one_user_and_create_pie():
    # if 'int_registered_user' not in session:
    #     User.flash_msg_must_login()
    #     return redirect('/login')
    # user = User.get_by_id(session['int_registered_user'])
    # session['signed_in_user_name'] = user.first_name + ' ' + user.last_name
#     Pie.get_pies_of_one_user(session['int_registered_user'])
#     return render_template('dashboard.html', pies = Pie.all_users_all_pies())

# ? Show one car based on user id
# @app.route('/pies/<int:id>')
# def show_one(id):
#     if 'int_registered_user' not in session:
#         User.flash_msg_must_login()
#         return redirect('/')
#     return render_template('show_pie.html', pies = Pie.get_one_pie_by_id_w_user(id))

# ? edit page for one car by using the user's id
# @app.route('/pies/edit/<int:id>')
# def edit_pie_page(id):
#     if 'int_registered_user' not in session:
#         User.flash_msg_must_login()
#         return redirect('/')
#     pie = Pie.get_one_pie_by_id_w_user(id)
#     session['current_pie_id'] = pie.id
#     session['current_pie_name'] = pie.name
#     return render_template('edit_pie.html', pie = pie)

# ? post method route to process updating the car data and validate it
# @app.route('/pies/update', methods=["POST"])
# def update_pie():
#     if session["current_pie_name"] == request.form['name']:
#         Pie.update(request.form)
#     print("------------Pie was UPDATED !!!!!!!!-------------")
#     return redirect('/dashboard')
#     if not Pie.validate_pie(request.form):
#         print(f'\n\n{session["current_pie_name"]}\n\n')
#         return redirect(f"/pies/edit/{request.form['id']}")
#     return redirect('/dashboard')

# ? deletes car data based on the car's id
# @app.route('/pies/delete/<int:id>')
# def delete(id):
#     if not Pie.validate_pie_deletion_through_url(id):
#         print(f"\n\nError! Can't delete pie, its not from your account!!!!!\n\n")
#         return redirect(f"/dashboard")
#     Pie.delete(id)
#     return redirect('/dashboard')