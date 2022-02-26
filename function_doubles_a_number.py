#Write a function called doubles() that takes one number as its input and doubles that number. Then use the doubles() function in a loop to double the number 2 three times, displaying each result on
#a separate line. Here is some sample output:
#4
#8
#16

def doubles(num):
    double_no = num*num
    return double_no

user_input = int(input("Enter a number: " ))    
result = doubles(user_input)
print(result)
