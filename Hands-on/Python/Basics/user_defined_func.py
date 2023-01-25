# def is the keyword used to create the custom function in py

# the function to check whether the given input object is negative or positive 

def sign(x): 
    if x > 0:
        return 'positive'
    elif x < 0: 
        return 'negative'
    else: 
        return 'neutral'
for x in [-1, 0, 1]:
    print(sign(x))      


# pass optimal arguments in a python function 


def hello(name, loud = False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s'  % name)  

hello('Roger')
hello('Fredrick', loud = True)
              