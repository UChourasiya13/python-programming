"""z = lambda x,y : x+y
print(z(2,4))"""

"""
list1 = [2,13,42,4,524,331,452,321,22]

list_even = []

print(list1)
print(list_even)

for i in list1 :
	y = even(i) 
	if y == True : 
		list_even.append(i)

print(list_even)"""
from functools import reduce
list1 = [2,13,42,4,524,331,452,321,22]
list_even = filter(lambda x : x%2==0,list1)
print(type(list_even))
list_odd = list(filter(lambda x : x%2!=0,list1))
list_even2 = list(map(lambda x : x*2,list_even))
sum = reduce(lambda x,y : x+y, list_even2)
print(list1)
print(list_even)
print(list_odd)
print(list_even2)
print(sum)