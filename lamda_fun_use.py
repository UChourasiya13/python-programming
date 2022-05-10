from functools import reduce
list1 = [1,13,42,524,331,452,321,22]

list_even = []

print(list1)
print(list_even)

#for i in list:
#    if i%2==0:
 #       list_even.append(i)
 #   print(list_even)

print("----------------filter----------------")

#filter 
#def even(n):
 #   return n%2==0
list1 = [2,13,42,4,524,331,452,321,22]
list_even = list(filter(lambda x : x%2==0,list1))
list_odd = list(filter(lambda x: x % 2 != 0, list1))
print(list1)
print(list_even)
print(list_odd)

print("---------------mapped-----------------")
#mapped
list_even = list(map(lambda x: x*2 , list_even))
print(list_even)

print("---------------reduced-----------------")
#reduced

sum = reduce(lambda x,y : x+y ,list_even)
print(sum)
print("--------------------------------")








