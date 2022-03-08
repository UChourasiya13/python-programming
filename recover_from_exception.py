# Ask the user to enter an integer.
# Repeat the process if the user hasn't entered an integer.

while True:
    try:
        input_num = int(input("Enter number : "))
        print(input_num)
        break
    except ValueError:
        print("try again")

        
