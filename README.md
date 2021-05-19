CPE-551
Final Project
Flask- SQL Alchemy -Blogging website


####Final Project Goal: Goal was to create a website where user can write his/her blog posting some text, image or video
####To create this website, I used flask framework and sql alchemy database to store the data .
###Features of the website

###Sign up
1. User can sign up and create an account
2. User should have unique email (Implemented Check)
3. User should have unique username(Implemented
Check)
4. User should have at least 8 characters length of
password (check implemented)
5. First name and Last name is mandatory
6. Success message to be displayed for successful login
7. Failure message to be displayed on login error
Stevens Institute of Technology
Author: Swapnil Gorey CPE-551- Final Project Student Id:10443462
 
###Login
1. User is able to login with email and password combination
2. User is able to sign in username and password combination
3. Success message to be displayed for successful login
4. Failure message to be displayed on login error

###Home Page
1. Home page is displayed once user is logged in and authenticated
2. User session is managed
3. All posts from all users are displayed on home page
with their author names and time stamp
4. User is able to edit and delete only their own post
5. Edit and delete buttons are hidden for posts for
which user is not the author
6. All posts are displayed in sorted order and scrollable

###Edit Post
1. While editing the post all the fields are being prepopulated
2. User is able to edit the fields
3. User is able to repost the edited post 4. Same post is being updated
Stevens Institute of Technology
Author: Swapnil Gorey CPE-551- Final Project Student Id:10443462

###Delete Post
1. User is able to delete the post
2. Once deleted the post entry is getting deleted
from database itself
Search
1. User is able to search for keywords from the title or from the post body and only those posts shows on the home page
2. If no post found with searched keyword, message shows up no posts found
###Logout
1. Once user hits log out button, user session is destroyed and user is redirected back to login page
2. When user logs back in and authenticated , all his data from the db gets populated again on home page.
Stevens Institute of Technology
Author: Swapnil Gorey CPE-551- Final Project Student Id:10443462

##How to Run

#####Go to final project folder and run these commands
##### pip install -r requirements.txt
##### python3 main.py