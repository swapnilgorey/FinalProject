from flask_login import UserMixin
from datastore_entity import DatastoreEntity, EntityValue
import datetime


class User(DatastoreEntity, UserMixin):
    id=EntityValue(1)
    email=EntityValue(None)
    username = EntityValue(None)
    password = EntityValue(None)
    firstName = EntityValue(None)
    lastName = EntityValue(None)
    password = EntityValue(None)
    __kind__ = "user"
    # date_created = EntityValue(datetime.datetime.utcnow())

    # other fields or methods go here...
    #def authenticated(self, password):
    #    ...









# import public as lb
# from werkzeug.security import generate_password_hash
#
#
# userData = {
#     u'email': "",
#     u'username': "",
#     u'firstName': "",
#     u'lastName': "",
#     u'password': ""
# }
#
# def adduser(formData):
#     userCollection = lb.db.collection(u'users')
#     usersColDoc = lb.db.collection(u'users').document()
#     usersColDocid = usersColDoc.id
#     userData[u'email'] = formData['email']
#     userData[u'username'] = formData['username']
#     userData['firstName'] = formData['firstName']
#     userData['lastName'] = formData['lastName']
#     userData['password'] = generate_password_hash(formData['password'], method="sha256")
#     lb.db.collection(u'users').document(usersColDocid).set(userData)
