#poo12

class Person:
    number_of_people = 0
    GRAVITY = -9.8
    
    
    def __init__(self, name):
        self.name = name
        
    
    @classmethod
    def number_of_people(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
p1 = Person('tim')
p2 = Person('jill')
print(Person.number_of_people)

