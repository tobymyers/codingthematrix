from GF2 import *
from random import randint
class Key:
    """creates a key as a list of GF2 objects"""
    def __init__(self, key_length):
        self.length = key_length
        gf2 = [0,one]
        self.list = [gf2[randint(0,1)]for i in range(self.length)]

    def get_length(self): return self.length

    def get_list(self): return self.list

    def save(self):
        """saves Key object to file as dictionary"""
        file = open('key_instance.py', 'w')
        file.write(str(self.list))
