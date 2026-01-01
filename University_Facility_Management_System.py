#Libraries 
import os
import csv

# Parent Class
class User:
    def __init__(self,name=None,id=None,role=None):
        self.name = name
        self.id = id
        self.role = role
        