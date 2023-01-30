# Inheritance means we can reuse the parent class code 

# Inheritance allows us to define a class which inherits all the methods and and properties from the parent class. 
# the parent/super class / base class is the class which gives all the methods and properties. 
# child class is the class that inherits from the parent super class 

class Person: 
    def __init__(self, firstname, lastname, age, country, city):
        # self allows to attach parameter to the class 
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        self.country = country
        self.city  = city 


# initialize the object 

p = Person('Amy', 'Ronald', 25, 'England', 'Surrey') 
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)


class Person: 
    def __init__(self, firstname ='Mary', lastname='Reagon', age = 28, country = 'United Kingdom', city='Manchester'):
        # self allows to attach parameter to the class 
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        self.country = country
        self.city  = city  
        self.skills = [] 

    def person_info(self): 
        return f'{self.firstname}, {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'

    def add_empskill(self, skill): 
        self.skills.append(skill)       


# initialize the object 

p1 = Person() 
print(p1.person_info())
p1.add_empskill('python')
p1.add_empskill('spark')
p1.add_empskill('Azure')
p2 = Person('Vanessa', 'Carey', 30, 'Barcelona', 'Spain')
p2.add_empskill('AWS')
p2.add_empskill('java')
p2.add_empskill('Mongodb')
print(p2.person_info())

# sub class / child class 

class Student(Person):
    pass # placeholder 

# we can call the constructor which we can access it through the parent properties by calling super() method

s1 = Student('Ema', 'Watson', 32, 'England', 'Oxford')
s2 = Student('Lisa', 'Brummel', 26, 'Scotland', 'Glasgow')
print(s1.person_info())
s1.add_empskill('javascript')
s1.add_empskill('Google Cloud')
s1.add_empskill('Docker')
print(s1.skills)

print(s2.person_info())
s2.add_empskill('Sales')
s2.add_empskill('Financial modelling')
s2.add_empskill('Analytics')
print(s2.skills)

# Method overriding 

class Student(Person):
    def __init__(self, firstname='Mary', lastname='Reagon', age=28, country='United Kingdom', city='Manchester', gender = 'female'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'She' if self.gender == 'female' else 'He'
        return f'{self.firstname},{self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}'

s1 = Student('Celine', 'Nash', 28, 'England', 'Cornwall', 'female')
s2 = Student('Angel', 'Gibbson', 31, 'Ireland', 'Belfast', 'male') 
print(s1.person_info())
s1.add_empskill('java')
s1.add_empskill('golang')
s1.add_empskill('cybersecurity')
print(s1.skills)

print(s2.person_info())
s2.add_empskill('Digital Marketing')
s2.add_empskill('Retail Banking')
s2.add_empskill('Sales')
print(s2.skills)
 


