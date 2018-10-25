#Excercise 5
'''
Take two lists, say for example these two:
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
'''
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if i in b and i not in c:
        print (i ," is common element.")
        c.append(i)

#create a random list
d = range(random.randint(0,30))
print (d)