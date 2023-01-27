# python uses try and except block to handle errors gracefully. A graceful exit or graceful termination of handling of errors
# can be done using the exception handling mechanism. In python we can achive it through try and except block. 
# try -- run the code
# except -- execute this code when there's an exception 
# else -- no expression run this code 
# finally -- always execute the code within this block 


a = [2, 3, 4]
try: 
    print("Second element = %d" %a(a[1]))

    #throws error since there's only three elements in the array 
    print("Fourth element= %d" %(a[3]))

except: 
    print("ArrayIndexOutOfBound exception occured")


# apply python except type error 
# apply typeerror, valuerror and zerodivisionerror in Python
try: 
    name = input('Enter your name: ')
    year_born = input('Enter your Birth year: ')
    age = 2023 - year_born
    print(f'You are {name}, and your age is {age}.')

except TypeError:
    print('Type error occurred') 

except ValueError: 
      print('Value error occurred ') 

except ZeroDivisionError: 
    print('Zero Division error occured')


