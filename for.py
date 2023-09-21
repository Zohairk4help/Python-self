
print("--------1. Do the following to create a program that simulates how websites ensure that everyone has a unique username.")

print(" \n Make a list of five or more usernames called current_users.")
current_users = ["abc@hotmail.com", "cba@aol.com", "cab@live.com", "bac@yahoo.com","acb@gmail.com"]
print("-------> current_users: " , current_users)

print(" \n Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.")
new_users = ["abc1@hotmail.com", "cba2@aol.com", "cab3@live.com", "bac@yahoo.com","acb@gmail.com"]
print("-------> new_users: " , new_users)

print ("\n Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.")
for x100 in new_users:
    if x100 in current_users:
        print(x100, "please print new username.")
    else:
        print(x100, "username is available")
print("\n Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.")
    #convert to lower and compare
current_users = [x100.lower() for x100 in current_users] 
new_users = [x100.lower() for x100 in new_users]
print("\n ref: https://stackoverflow.com/questions/44633734/case-insensitive-list-item-comparison-python")

print("\n -------------2. Color probability--------------") 

#You're playing a game with a friend involving a bag of marbles. In the bag are ten marbles:

#1 smooth red marble -----> 1/10 (0.10 probability)

#4 bumpy red marbles  -----> 4/10 (0.40 probability)

#2 bumpy yellow marbles  -----> 2/10 (0.20 probability)

#1 smooth yellow marble -----> 1/10 (0.10 probability)

#1 bumpy green marble -----> 1/10 (0.10 probability)

#1 smooth green marble -----> 1/10 (0.10 probability)


number_total_marbles = ["smooth red", "bumpy red","bumpy red", "bumpy red","bumpy red","bumpy yellow", "bumpy yellow", "smooth yellow", "bumpy green","smooth green"]
texture = ["smooth", "bumpy"]
colour_total_marbles = ["red", "red","red", "red","red","yellow", "yellow", "yellow", "green","green"]
colour = ["yellow", "red", "green"]
print("________please pick the texture and the colour from their lists: colour", colour, "texture ", texture, "______")

x1 = input("please type in the texture and the colour to get its probability  ")



count3=len(number_total_marbles)
nminus1= count3-1
print(count3, "total number of marbles balls in a bag")
countcolour=colour_total_marbles.count(x1)
print(countcolour, "is the total number of",x1,"colour of the selected ball")


for x1 in number_total_marbles:
    if x1 == "bumpy red" :
        print(5/nminus1 , "probability for", x1, "marbles".format(.2))
    elif x1 == "smooth red":
        print(round(1/nminus1), "probability for", x1, "marbles")
    elif x1 == "bumpy yellow":
        print(2/nminus1, "probability for", x1, "marbles")
    elif x1 == "smooth yellow":
        print(1/nminus1, "probability for", x1, "marbles")
    elif x1 == "smooth green":
        print(1/nminus1, "probability for", x1, "marbles")
    else:
        print(1/nminus1, "probability for", x1, "marbles")




print("\n As a complete example, color_probability('red', 'bumpy') should return the string '0.57'.")



print("--------3. Write an if-elif-else chain that determines a person’s stage of life.")

#Set a value for the variable age, and then:
age = int(input(" PLEASE TYPE IN YOUR AGE "))
#If the person is less than 2 years old, print a message that the person is a baby.

if age < 2 :
    print(" You are a Baby!!!!")

#If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
elif age <= 4 :
    print("You are a Todler.")

#If the person is at least 4 years old but less than 13, print a message that the person is a kid.
elif age in range (4, 13):
    print("You are a Kid.")

#If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
elif age <= 20:
    print("You are a Teenager.")

#If the person is at least 20 years old but less than 65, print a message that the person is an adult.
elif age < 65:
    print("You are an Adult.")

#If the person is age 65 or older, print a message that the person is an elder.
else:
    print("You are an Elder")




xbla = [1,2,3]
for item in xbla:
    pass  