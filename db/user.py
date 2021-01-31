from db.db import connect
from bson.objectid import ObjectId

class User():
    def __init__(self):
        self._user = connect('User')

    def insert_user(self,user):
        return self._user.insert_one(user)
    def get_user_by_email(self,email):
        user = self._user.find_one({'email':email})
        return user
    def get_user_by_id(self,id):
        user = self._user.find_one({'_id':ObjectId(id)},{'password':0,'_id':0})
        return user

