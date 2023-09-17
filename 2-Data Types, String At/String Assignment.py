#1. Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.

first_name = input("What is your name? (no caps)")
last_name = input("What is your surname? (no caps)")
print("Hello ", first_name.capitalize(), last_name.capitalize(),"! \n I hope you find everything okay! \n ^_^")

print("\n Another Reference link: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-13.php")


#2. Ask the user to type in the first line of a poem Raven by Edgar Allen Poe and display the length of the string. 
# Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1). Here is the poem Raven:

print("\n Poem 'Raven' by Edgar Allen Poe")

print("\n Deep into that darkness peering,")

print("Long I stood there, wondering, fearing,")

print("Doubting, dreaming dreams no mortals")

print("Ever dared to dream before;")

print("But the silence was unbroken,")

print("And the stillness gave no token,")

print("And the only word there spoken")

print("Was the whispered word, 'Lenore!'")

print("This I whispered, and an echo")

print("Murmured back the word, 'Lenore!'")

print("Merely this, and nothing more.")


first_line = input("\n What is the first line of a poem 'Raven' by Edgar Allen Poe? (type in please)")
print("The first letter of the poem's line is:" ,first_line[0])
print("The last letter of the selected line from the poem is:", first_line[-1])
print("Your input from a line of the poem is:", first_line.capitalize()," \n ^_^")


#3. Removes extra characters from the start and end of a string and explain why you need to remove white spaces while exploring text.
print("\n This is the white-space free dsiplay of the same line from the poem:", first_line.strip())
print("\n Why we removed whitespace? The reason why we remove it is because Python process these white space and if we have no idea about white spaces, there cannot properly process the text.")

