from flask import Blueprint, render_template,request,flash
from flask_login import login_required,current_user
from .models import Post, User
from public import db
pages = Blueprint('pages',__name__)

@pages.route('/', methods=['GET'])
@login_required
def home():
    posts=Post.query.all()
    users=User.query.all()
    for post in posts:
        print(post.postData)
    return render_template("home.html",user=current_user,posts=posts, users=users)

# @pages.route('/deletePost',methods=['GET','DELETE'])
# @login_required
# def deletePost():
#
#         id=request.form.get(id)
#         post=Post.query.all(id=id)
#         print (post)
#     return render_template("addPost.html", user=current_user)

@pages.route('/addPost',methods=['GET','POST'])
@login_required
def addPost():
    if request.method=='POST':
        postTitle=request.form.get('postText')
        postText=request.form.get('postText')
        imgurl= request.form.get('img')
        videourl=request.form.get('video')

        if len(postText)<1:
            flash("Please Write Something Before You Post", category='error')
        else:
            newpost=Post(postTitle=postTitle,postData=postText,imgurl=imgurl,videourl=videourl,user_id=current_user.id)
            db.session.add(newpost)
            db.session.commit()
            flash("Successfully Added the Post", category='success')

    return render_template("addPost.html",user=current_user)