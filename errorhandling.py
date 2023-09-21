print("1- Let us define a division operation inside a function (using def) but to get an error, define the denominator as 0. So, type except statement properly.")

try:
    denominator = int(input('Please enter a number for denomina 0:\n'))
    numerator = int(input('please enter the number 0'))
    def division(bla):
        bla = numerator/denominator
        return bla 
    try:
        #numerator = int(input('please enter the number 0'))
        print(f'division of {numerator} by {denominator} is {numerator/denominator}')
    except ZeroDivisionError:
        print(f'You entered {numerator}, which is not a possible number.')
except NameError:
    print('You are supposed to enter number >0 for easily divisione.')
except:
    pass

# ref: https://blog.enterprisedna.co/python-try-except/

print("\n 3- Please define a function and with this function, generate a ValueError exception simply by entering a string instead of numerical value.")

import math
def my_function(a):
   return math.sqrt(a)
try:
    a = int(input('Please enter a positive number:\n'))
    try:
        print(f'Square Root of {a} is {math.sqrt(a)}')
    except ValueError as ve:
        print(f'You entered {a}, which is not a positive number.')
except ValueError as ve:
    print('You are supposed to enter positive number.')

# ref: https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples

print("\n 4- Write a function called circumference that takes the diameter of a circle as input and produces the circumference of the circle. Your function should use try...except to check for a type error in the event a string is passed.")

