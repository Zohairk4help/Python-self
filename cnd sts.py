print("#1: Ask the user to enter a number between 10 and 20 (inclusive).")
print("If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”.")

num = int(input("Enter a number: (between 10 - 20) "))
if num in range(10,20):   
    print ("Thank You")
else :
    print ("incorrect answer") 

print("\n other ref: https://stackoverflow.com/questions/12140185/using-in-range-in-an-if-else-statment")

print("-------------------------------------------------------------------------------------------------------------")


print("#2- In this exercise, you will create a program that reads a letter of the alphabet from the user. According to the answer:")


#If the user enters a, e, i, o, u, then your program should display a message indicating that the entered letter is a vowel.


#if the user enters y, then your program should display a message indicating that y is sometimes a vowel and sometimes a consonant.

#Otherwise, your program should display a message indicating that the letter is a consonant.

input = input("Input a letter of the alphabet: ")

if input in ('a', 'e', 'i', 'o', 'u'):
	print(input, "is a vowel." )
elif input == 'y':
	print(input, "is Sometimes vowel and sometimes consonant.")
else:
	print(input, "is a consonant." ) 