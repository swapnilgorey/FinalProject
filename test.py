import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('/Users/swapnilgorey/Downloads/escribblethoughts-firebase-adminsdk-m5nce-505bca4dc4.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'docs').get()
for doc in doc_ref:
    print (str(doc.to_dict()))
# query = doc_ref.where(u'Authour', u'==',u'Swapnil' )

# print(query.stream())


# docs = db.collection(u'docs').where(u'Authour', u'==', 'Swapnil').stream()
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')



# docs = db.collection(u'docs').get()
# if len(docs)==0:
#     db.collection(u'docs').document(doc_id).set({
#         "post":"My Test Post",
#         "Authour":"Swapnil"
#     })
# for doc in docs:
#     print (doc.to_dict())
