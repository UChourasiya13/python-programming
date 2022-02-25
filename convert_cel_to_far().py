#convert_cel_to_far() which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:
#F = C * 9/5 + 32

def convert_cel_to_far(c):
    F= c * 9/5 + 32
    return float(F)

temp = float(input("Enter Temperature in celcius: "))
result = convert_cel_to_far(temp)
print(f"Temperature in Fahrenheit : {result:,.2f}")
