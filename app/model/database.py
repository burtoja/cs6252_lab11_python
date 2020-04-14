'''
Created on Mar 25, 2020

@author: CS6252
'''
import json
from app.model.user import User

class Database:
    """ A database simulation """
    
    def __init__(self):
        self.users = []
        users = []
        try:
            with open("app/model/users.json", "rt") as user_file:
                users_json_string = user_file.read()
                users_wrapped = json.loads(users_json_string)
                users = users_wrapped["users"]
        except:
            print("reading from users.json failed")
        
        for user in users:
            user_obj = User(user["email"], user["name"], user["password"])
            self.users.append(user_obj)


    def get_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
            
        return None
    
    
    def add_user(self, user):
        self.users.append(user)
        
        users = []
        for user in self.users:
            user_dict = {"email": user.email, "name": user.name, "password": user.password}
            users.append(user_dict)
            
        try:
            with open("app/model/users.json", "wt") as user_file:
                user_file.write(json.dumps({"users": users}))
        except:
            print("writing to file users.json failed")
            return False
        
        return True
        