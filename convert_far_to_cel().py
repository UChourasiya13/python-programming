#convert_far_to_cel() which take one float parameter representing
#degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula:
#C = (F - 32) * 5/9

def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    return float(C)

temp = float(input("Enter Temperature in Fahrenheit: "))
result = convert_far_to_cel(temp)
print(f"Temperature in Celsius : {result:,.2f}")
