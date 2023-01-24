from datetime import datetime
import os

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

## lambda is used to create anonymous functions
# clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def greet(name):
    clear()
    if current_time > '05:00:00' and current_time < '11:59:59':
        print("Good morning " + name + "!")
    elif current_time > '12:00:00' and current_time < '16:59:59':
        print("Good afternoon " + name + "!")
    else:
        print("Good evening " + name + "!")

def cube(num):
    result = num*num*num
    return result

name = input('Say your name: ')
age = int(input('Now your age: '))

cubed_age = cube(age)
    
greet(name)
print('Your age cubed is: ' + str(cubed_age))
