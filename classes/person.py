

class Person(object):
    """Person class
    
    Defines as person in the system
    """
    count = 1
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 
        self.staff_id = "ST-"+str(Person.count)
        self.allocated_office = ""
        #increment count of person class by one
        Person.count += 1


class Staff(Person):
    """Staff class
    
    Inherits from the person class and defines a person as 
    a spcific staff member in the system
    """
    pass 


class Fellow(Person):
    """Fellow class

    Inherits from the person class and defines a person as 
    a specific fellow in the system 
    """

    count = 1
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.allocated_livingspace = ""
        self.staff_id = "FL-"+str(Fellow.count)
        #increment count of fellow class by one
        Fellow.count += 1



        
