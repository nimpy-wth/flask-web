from flask import Blueprint, render_template, request

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        user_name = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(user_name) < 2:
            pass 
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            pass

    return render_template("signup.html")