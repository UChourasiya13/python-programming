#Write a function called cube() with one number parameter and returns the value of that number raised to the third power. Test the function by displaying the result of calling your cube() function on
#a few different numbers

def cube(x):
    """finding area of cube"""
    Area = x*x*x
    return Area



area = cube(int(input("Enter a number to find the area of cube: ")))
print(f"Area of cube is : " , area)
