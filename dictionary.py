#Dictionaries:

#The key is the fruit name and the value is the number so now if we want to extract, insert, change values we do it as follow:
FOOdMenue = {'apple' : 1, 'orange' : 2 , 'Banana' : 3}
print ("The dictionary is: " , FOOdMenue )

#Extract value:
#This will return the value 1
print ("The value of apple is:" , FOOdMenue['apple'], "\n" )

#Inserting  a new value to the dictionary:
#Note that the key is unique but not the value  so now we will have additional key with same value as Banan
print ("Adding key strawberry")
FOOdMenue['strawberry'] = 3
print (FOOdMenue)

#Change value of a key:
print ("Chnging the value of key straberry.")
FOOdMenue['strawberry'] = 4
print(FOOdMenue)

print ("Return all the keys only:", FOOdMenue.keys() ,"\n" )
print ("Return all the values only:", FOOdMenue.values() )

#Delete value:
#del FOOdMenue['apple']
#print ("Return all the keys only after deleting apple:", FOOdMenue.keys() ,"\n" )


#Looping the dictionary:

for i in FOOdMenue:
	print (i, FOOdMenue[i] )
