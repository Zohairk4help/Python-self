print("#1: Suppose you invested in Bitcoin at the end of 2020 when Bitcoin gained a lot of value. What would be your money at the end of a week if you had invested $1000 with an average daily increase of 12% ? You can solve the problem using Python.")

#Variables:

initial_capital= 1000

daily_growth= 12

time_period= 7

final_growth_rate= daily_growth/100

result= initial_capital*(1+final_growth_rate)**time_period

print("Answer #1:" , result)

print("\n #2: Print the text in quotes with Python. However, you must get the numbers from variables using .format() notation. Because the text is long, you might consider writing in two lines:")


print("\n Answer #2) :When we buy bitcoin with {} USD at the beginning of the week,\n we would earn {:.2f} USD at the end of the week, with an average gain of {}%.".format(initial_capital, result, daily_growth))


print("\n----------other reference help: https://www.geeksforgeeks.org/python-string-format-method/--------------------------")

print("\n Answer #3): Get the temperature in Fahrenheit from user and write a code to convert it to Celcius. For conversion, you can use this formula: C = (5/9) * (F - 32)")

print("\n ---------------Enter the temperature in Fahrenheit:-----------")


farenheit_number = input("please type in a temperature value in Farenheit: (for e.g: 26) ")
f_number_user = int(farenheit_number)
Celcius_conversion = (5/9)*(f_number_user-32)
print("Hello! the output in Celcius: ", Celcius_conversion,".")

print("\n----------other reference help: https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/-----------------------------")

print("\n #4) Get a three digit number the from user and calculate the sum of the digits in the integer.")
# Function to get sum of digits 
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = input("please type in a number (for example: 365) ")
print(getSum(n))

print("\n----------other reference help: https://www.geeksforgeeks.org/python-program-for-sum-the-digits-of-a-given-number/--------")


print("\n #5- Write some code to calculate the hypotenuse of a right angled triangle. Get the side lengths from the user.")

first_side = input("please type in a value of the 1st side of the triangle: (for e.g: 6) ")
firstside_user = int(first_side)
sec_side = input("please type in a value of the 2nd side of the triangle: (for e.g: 8) ")
secside_user = int(sec_side)
import math 
hypot_triangle_comp = math.sqrt(firstside_user**2+secside_user**2)
print("The value of Hypotenuse: ", hypot_triangle_comp,".")