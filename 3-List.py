print("#1) Write a code to compute the sum of the two lowest numbers and the two highest numbers in the following list.")

my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
my_list.sort()
print(my_list, "is the asc order")
print(my_list[0]+my_list[1], "is the addition of the two lowest numbers.")
print(my_list[-1]+my_list[-2], "is the addition of the two highest numbers.")

print("------------------------------------------------------------------------------")

print("\n #2) The following two lists contain student names and scores. Write a code that gets the name from the user and prints the score of that student.")

names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

user_input= int(input("please type in the lists' single index number, example: 2"))

print("For the student,", names[user_input], ",the score:" , scores[user_input])

print("------------------------------------------------------------------------")
print("\n #3) By using the two lists above, what is the maximum score and how many students got that score?")

sc_copy = scores.copy()
sc_copy.sort()

print(sc_copy, "is the ascending order of the score-list")


maxvalue= max(sc_copy)
print(maxvalue, "is the max score that a student got and there is/are: ",  sc_copy.count(maxvalue), "student that got max score")

do= sc_copy.index(maxvalue)
done = int(do)
print(do, "is the index number of the max score and the name of the student is", names[done], "that got,", scores[done],".")





album = "Flip Your Wig"


print(album[10:])