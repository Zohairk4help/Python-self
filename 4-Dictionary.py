print("#1) Create a dictionary with 7 days. Ask the user to choose 2 different days by listing the (e.g. '12' for Monday and Tuesday). Delete the user-selected days from the dictionary and print the remaining 5 days on the screen.")

days_dict = {'Monday':19,'Tuesday':22, 'Wednesday':16, 'Thursday':13, 'Friday': 12, 'Saturday':0, 'Sunday':0}
user_input = input("Please type in the number when there no workers in the office:  ")
user_inputdig = int(user_input)

 
# one-liner
print("The day/s where there was no workers in the office is/are :", list(days_dict.keys())
      [list(days_dict.values()).index(user_inputdig)])
#other ref: https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/

print("\n to check the dictionary after deleting Saturday:" )
popped_item1 = days_dict.pop('Saturday')
print(days_dict, "\t\n Sunday is still there!!!")

popped_item2 = days_dict.pop('Sunday')
print(days_dict, "\t\n The dict that has all the numbers except '0'")


print("-------------------------------------------------------------------------------")

print("#2) Create a dictionary with the following personnel. Use names as keys.")

personnel_dict= {'Michael' : ['age 20'], 'Linda': ['age 30']}
print(personnel_dict)
 
print("-------------------------------------------------------------------------------")

print("#3) Add child information to Michael and Linda. Michael has two children (Karen (age : 12, female) and Greg (age : 7, male) and Linda has one child (Susan (age: 6, female))")


#childrenM= 

child1 = {'Karen','age: 12', 'female'}
child2 = {'Greg','age: 7', 'male'}

#childrenL= 
child3= {'Susan', 'age 6', 'female'}

personnel_dict.update({'Micheal':['age 20',child1,child2], 'Linda':['age 30', child3]})


print("---------------------------------------------------------------------------------")
print("#4) Print the names of Michael's children in a list.")

print("\n", personnel_dict, "is the updated dict")