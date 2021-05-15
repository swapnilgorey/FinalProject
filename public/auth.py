import public
import uuid
from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)



@auth.route('/login',methods=['GET','POST'])

def login():
    userCollection = public.db.collection(u'users')
    if request.method == 'POST':
        email=request.form.get('email')
        password = request.form.get('password')

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

@auth.route('/logout')
@login_required
def logout():
    # return render_template("home.html")
    login_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        username=request.form.get('username')
        firstName = request.form.get('fisrtname')
        lastName = request.form.get('lastname')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        userCollection = public.db.collection(u'users')
        usersColDoc = public.db.collection(u'users').document()
        usersColDocid = usersColDoc.id


        userData = {
            u'email': "",
            u'username': "",
            u'firstName': "",
            u'lastName': "",
            u'password': ""
        }
        users = userCollection.get()
        dataCheck=True
        if len(users)!=0:
            for user in users:
                userdict=(user.to_dict())
                if userdict['email']==email:
                    # print('Account for this email already exist. Please try something else.')
                    flash ('Error: Account for this email already exist. Please try something else.', category='error')
                    dataCheck = False
                elif userdict['username']==username:
                    # print(' Username already been taken, Try something else')
                    flash('Error: Username already been taken, Try something else', category='error')
                    dataCheck= False


        if (len(firstName)<1):
            # print(' First name cannot be empty')
            flash('Error: First name cannot be empty', category='error')
            dataCheck = False
        if (len(lastName) < 1):
            # print (' Last name cannot be empty')
            flash('Error: Last name cannot be empty', category='error')
            dataCheck = False
        if password!=password2:
            # print ('Password do not match')
            flash('Error: Passwords do not match', category='error')
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
            flash('Account created Successfully', category='success')
            return redirect(url_for("pages.home"))


    return render_template("register.html")