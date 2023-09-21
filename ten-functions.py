print("---------1. Finding Prime Number------------------------------")
numberinput =int(input("Please type a number to determine whether it's prime or not:  "))
# I combined if-elif and def function with multple arguments inside the parameters to get the Prime Number.
# the idea is taken from the web: https://www.chilimath.com/lessons/introductory-algebra/prime-factorization-of-an-integer/

def determine_prime_function(numberinput):
    return (numberinput>1 , numberinput%1 ==0, numberinput%numberinput==0 , numberinput != 1, numberinput%2!=0, numberinput%3!=0)
if 2<= numberinput <= 3:
    print(determine_prime_function(numberinput), "is a", True, " PRIME #")
elif numberinput>1 and 0 == numberinput%1 and numberinput%numberinput==0 and numberinput != 1 and numberinput%2!=0 and numberinput%3!=0:
        print(determine_prime_function(numberinput), "is a", True, "Prime #---")
else:
    print(determine_prime_function(numberinput), "is not a Prime #/-", False)


print("\n ------------2. Rømer temperature---------------------")

# Rømer = (Celsius / 1.9047619) + 7.5 ----> formula [web: https://www.metric-conversions.org/convert/1/175/24]

cel = int(input("type in numbers, e.g: 24:  "))
def celsius_to_romer(cel):
     return ((cel / 1.9047619) + 7.5 ) 
print("{:.2f}".format(celsius_to_romer(cel)))

print("\n ------------3. Pixelart planning--------------------")

dividend = int(input("type in numbers for the size of the wall 'in milimeters', e.g: 4050:  "))
divisor = int(input("type in numbers for the size of pixel 'in milimeters, e.g: 27:  "))


def is_divisible(dividend, divisor):
     return (dividend%divisor==0)

print(is_divisible(dividend, divisor))

# web ref: https://www.30secondsofcode.org/python/s/is-divisible/
print("------------------------------------------------------------")
