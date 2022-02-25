#check enter year is leap or not!!!
year =int(input("Enter a year: "))
if (year%400==0):
    print("Year is a leap year")
elif(year%100==0):
    print("Year is not a leap year")
if (year%4==0):
    print("Year is a leap year")
else:
    print("Year is not a leap year")
    
    
