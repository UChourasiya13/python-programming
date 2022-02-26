#write a program to add global and local values !!

glob_num = int(input("Enter a numeber: "))

def outer_func():
    outer_num = int(input("Enter another numeber: "))
    def inner_func():
        sum_of_num = outer_num + glob_num
        return  sum_of_num
    return inner_func()

result = outer_func()
print(result)
