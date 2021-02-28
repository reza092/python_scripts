# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Why do you need the map function?
# > pass a function to every single element in the list.

def square(num):
    return num*2

my_nums = [1,2,3,4]

for item in map(square, my_nums):
    print(item)
    
y = list(map(square, my_nums))
print(y)

# Filter does the same but return if the function is satisfied
def check_even(num):
    return num%2 == 1

#for n in filter(check_even, my_nums):
 #   print (n)

print(list(filter(check_even, my_nums)))

# lambda expression
check_even2 = (lambda num: num%2 == 0)
print(list(filter(lambda num: num%2 == 0, my_nums)))

## Test: grab the first letter of words from the following line
mylist = ("I can not go anywhere")
mylist.split()

#lambda word: word[0], mylist.split()

print(list(map(lambda word: word[0], mylist.split())))