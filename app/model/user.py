'''
Created on Mar 25, 2020

@author: CS6252
'''
class User():
    """ tracks a user """

    def __init__(self, email, name, password):
        '''
        Constructor
        '''
        self.email = email
        self.name = name
        self.password = password
        