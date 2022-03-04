#Write a script that prompts the user to enter a word using the input() function, stores that input in a variable,
#and then displays whether the length of that string is less than 5 characters, greater than 5 characters, or equal to 5 characters by using
#a set of if, elif and else statements

ent_str = input("Enter a string: ")
store_str = len(ent_str)
if store_str==5:
    print("Entered string is equal to 5 character")
elif store_str<5:
     print("Entered string is less than 5 character")
else:
    print("Entered string is greater than 5 character")
    
    
