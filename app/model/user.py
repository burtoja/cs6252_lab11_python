'''
Created on Mar 25, 2020

@author: CS6252
'''
from flask_login.mixins import UserMixin

class User(UserMixin):
    """ tracks a user """

    def __init__(self, email, name, password):
        '''
        Constructor
        '''
        self.email = email
        self.name = name
        self.password = password
    
    def get_id(self):
        return self.email        