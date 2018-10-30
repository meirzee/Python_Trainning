#excersice 6 

stringA = input ("please specify a word :")
stringB = reversed(stringA)
stringC = []

print ("string a is: ", stringA)

for i in stringB:
    stringC.append(i)

str1 = ''.join(str(e) for e in stringC)
print ("The reversed form is", str1)

if str1 == stringA:s
    print ("The word is a palindrom.")
else:
    print ("It is not a palindrom")