import public as lb
from werkzeug.security import generate_password_hash


userData = {
    u'email': "",
    u'username': "",
    u'firstName': "",
    u'lastName': "",
    u'password': ""
}

def adduser(formData):
    userCollection = lb.db.collection(u'users')
    usersColDoc = lb.db.collection(u'users').document()
    usersColDocid = usersColDoc.id
    userData[u'email'] = formData['email']
    userData[u'username'] = formData['username']
    userData['firstName'] = formData['firstName']
    userData['lastName'] = formData['lastName']
    userData['password'] = generate_password_hash(formData['password'], method="sha256")
    lb.db.collection(u'users').document(usersColDocid).set(userData)
