

class Person(object):
    count = 1
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 
        self.staff_id = "ST-"+str(Person.count)
        self.allocated_office = ""
        Person.count += 1
        
