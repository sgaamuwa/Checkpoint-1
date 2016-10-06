import os


class Person(object):

    allocated_office = ""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 
    
    def save(self):
        pass 

    def request_reallocation(name, room):
        return ""

    def print_unallocated():
        return "" 