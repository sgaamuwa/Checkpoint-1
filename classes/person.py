

class Person(object):
    count = 1
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 
        self.staff_id = "ST-"+str(Person.count)
        self.allocated_office = ""
        Person.count += 1


class Staff(Person):
    pass 


class Fellow(Person):

    count = 1
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.allocated_livingspace = ""
        self.staff_id = "FL-"+str(Fellow.count)
        Fellow.count += 1



        
