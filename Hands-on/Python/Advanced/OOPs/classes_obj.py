# Python is an object oriented language 

# A class is a user-defined blueprint or prototype from which objects are created. 
# classes provide3 a means for bundling the data and functionality together. 
# Creating the class creates a new type of object, allowing new instances of that type to be made. 
# Each class instance can have attributes attached to it maintaining its state. 
# class instances can also have methods for modifying their state 

class Person: 
    pass 

# a class is a blueprint of an object. 
# In python, a number, string, list, dictionary, tuple, set etc. are objects of a built-in class. 
# A class is like an object constructor
# A class is a blueprint of objects where we instantiate it to create an object. 
# the class defines attributes and the behaviour of the object. 

# create an object by calling the class 

p = Person()
print(p)

# class constructor 

# In python, a constructor function is used make class as to be more useful. Python has built-in init() constructor function. 
# the init constructor has self parameter which is a reference to the current instance of the class. 

class Person: 
    def __init__(self, name):
        #self allows to attach the parameter to the class 
        self.name = name

p = Person('John')
print(p.name)
print(p) 

# add more parameters to the Person class constructor 

class Person: 
    def __init__(self, firstname, lastname, age, country, city):
        # self allows to attach parameter to the class 
        self.firstname = firstname
        self.lastname  = lastname
        self.age       = age
        self.country   = country
        self.city      = city


p = Person('Amy', 'Ronald', 25, 'England', 'Surrey')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.city)
print(p.country)

# object methods
# the methods are functions which belong to the object
class Person: 
    def __init__(self, firstname, lastname, age, country, city):
        # self allows to attach parameter to the class
        self.firstname = firstname
        self.lastname  = lastname
        self.age       = age 
        self.country   = country
        self.city = city 
    def person_info(self): 
        return f'{self.firstname}{self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'

p = Person('Amy', 'Ronald', 25, 'England', 'Surrey')
print(p.person_info()) 

# object default method 

class Person: 
    def __init__(self, firstname = 'Mary', lastname = 'Reagon', age=28, country='UK', city='Cambridge'):
        # self allows to attach parameter to the class
        self.firstname = firstname
        self.lastname  = lastname
        self.age       = age 
        self.country   = country
        self.city = city 
    def person_info(self): 
        return f'{self.firstname}{self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'


p1 = Person()
print(p1.person_info())
p2 = Person('Vanessa', 'Carey', 30, 'Lisbon', 'Portugal')
print(p2.person_info())


# Method to modify class Default values 

class Person: 
    def __init__(self, firstname = 'Mary', lastname = 'Reagon', age=28, country='UK', city='Cambridge'):
        # self allows to attach parameter to the class
        self.firstname = firstname
        self.lastname  = lastname
        self.age       = age 
        self.country   = country
        self.city = city 
        self.skills = []
    def person_info(self): 
        return f'{self.firstname},{self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'

    def add_empskill(self, skill): 
        self.skills.append(skill)


 # initialize the class objects 

p1 = Person()
print(p1.person_info())
p1.add_empskill('python')
p1.add_empskill('java')
p1.add_empskill('mongodb')
p1.add_empskill('sql')
p2 = Person('Vanessa', 'Carey', 30, 'Lisbon', 'Portugal')
print(p2.person_info())
p2.add_empskill('Azure')
p2.add_empskill('javascript')
p2.add_empskill('Spark')
print(p1.skills)
print(p2.skills)
        

        


        
