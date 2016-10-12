

class Person(object):
    """Person class
    
    Defines as person in the system
    """
    def __init__(self, first_name, last_name, staff_id):
        self.first_name = first_name
        self.last_name = last_name 
        self.staff_id = staff_id
        self.allocated_office = ""
    

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

    def __init__(self, first_name, last_name, staff_id):
        super().__init__(first_name, last_name, staff_id)
        self.allocated_livingspace = ""



        
