from people.person import Person

class Fellow(Person):

    count = 1
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.allocated_livingspace = ""
        self.staff_id = "FL-"+str(Fellow.count)
        Fellow.count += 1
    
