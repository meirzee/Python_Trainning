#Excecise3.py

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = int(input("Please select a number:" ))

for i in a:
    if i < 5:
        print (i)
        b.append(i)
    elif i < c:
        print (i)


print (b)
