<<<<<<< HEAD
import public
import uuid
=======
# import public
from .models import User
>>>>>>> origin/master
from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from public import db
from flask_login import login_user, login_required, logout_user,current_user

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])

def login():
    # userCollection = public.db.collection(u'users')
    if request.method == 'POST':
        email=request.form.get('email')
        password = request.form.get('password')
<<<<<<< HEAD

        users = userCollection.get()
        if len(users) != 0:
            for user in users:
                userdict = (user.to_dict())
                if userdict['email'] == email or userdict['username'] == email:
                    if check_password_hash(userdict['password'],password):
                        loggedInUser=User(id=userdict[id],email=userdict['email'],username=userdict['username'],firstName=userdict['firstName'],lastName=userdict['lastName'],password=generate_password_hash(password, method="sha256"))
                        flash('Successfully Signed In',category='Success')
                        login_user(loggedInUser, remember=True)
                        return redirect(url_for("pages.home"))
                    else:
                        flash('Wrong Password, Please Try again', category='error')
                        return render_template("login.html")
                else:
                    flash('No Account Exist with this Email', category='error')
                    return render_template("login.html")

    return render_template("login.html")
=======
        LoggedInUser=User.query.filter_by(email=email).first() or User.query.filter_by(username=email).first()
        if LoggedInUser:
            if check_password_hash(LoggedInUser.password,password):
                flash("Logged In Successfully!!", category='success')
                login_user(LoggedInUser,remember=True)
                return redirect(url_for("pages.home"))
            else:
                flash("Incorrect Username or Password, Try Agian!!", category='error')
        else:
            flash("No user exist with this email or username!!", category='error')
    return render_template("login.html",user=current_user)
>>>>>>> origin/master

@auth.route('/logout')
@login_required
def logout():
<<<<<<< HEAD
    # return render_template("home.html")
    login_user()
    return redirect(url_for('auth.login'))
=======
    logout_user()
    return redirect(url_for("auth.login"))
>>>>>>> origin/master

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        username=request.form.get('username')
        firstName = request.form.get('fisrtname')
        lastName = request.form.get('lastname')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        newuser=User(email=email, username=username,firstName=firstName,lastName=lastName,password=generate_password_hash(password, method='sha256'))
        emailExist=User.query.filter_by(email=email).first()

        usernameExist=User.query.filter_by(username=username).first()
        if emailExist:
            flash('Error: Account for this email already exist. Please try something else.', category='error')
        elif usernameExist:
            flash('Error: Username already been taken, Try something else', category='error')
        elif (len(password)<8):
            flash('Error: Password Length should be atleast 8 characters', category='error')
        elif password!=password2:
            # print ('Password do not match')
            flash('Error: Passwords do not match', category='error')
<<<<<<< HEAD
            dataCheck = False

        if dataCheck==True:
            # newUser= User(email=email,username=username,firstName=firstName,lastName=lastName,password=generate_password_hash(password, method="sha256"))
            # newUser=User
            id=uuid.uuid1()
            userData[u'id']=str(id)
            userData[u'email']=email
            userData[u'username'] = username
            userData['firstName'] = firstName
            userData['lastName'] = lastName
            userData['password'] = generate_password_hash(password, method="sha256")
            public.db.collection(u'users').document(usersColDocid).set(userData)
            # print(type(id))
            # id=uuid.UUID(bytes=id.bytes)
            # print(type(id))
            newUser = User(id=int(id),email=email, username=username, firstName=firstName, lastName=lastName,password=generate_password_hash(password, method="sha256"))
            login_user(newUser, remember=True)
=======
        else:
            db.session.add(newuser)
            db.session.commit()
>>>>>>> origin/master
            flash('Account created Successfully', category='success')
            return redirect(url_for("auth.login"))

    return render_template("register.html",user=current_user)