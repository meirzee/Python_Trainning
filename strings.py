import string;

message = "neW strinG"
print ("Following is the string: ", message)
STRING_LENTH = len(message)
print ("The string lenth is: ", STRING_LENTH )

#print (message.upper())
print ("The original str is: ", message)
print ("String upper case is: ",message.upper())
print ("String lower case is: ",message.lower(), '\n')


# Asigning the uper case format to the variable
message = message.upper()
print ("The new assigned format to string is: ", message)

print ("The capitalize format: ", message.capitalize())
#print ("The capwords format is: ", message.capwords() )
print ("Spliting the string will create a list of two string since the default delimiter is space: " ,message.split())
print (string.capwords(message))

#Definning a list
numlist = [1,2,3,4,5]
print ("The list is: ", numlist )
numlist.reverse()
print ( "The reversed list is :", numlist )

#if we want to reverse back we simply need to type the same command again:
numlist.reverse()

#Adding an adition list 
numlist2 = [6,7,8,9,10]

#appending numlist2 as additional one element into the first numlist
numlist.append(numlist2)
print ( "Now numlist is: ", numlist )
#now we got nested list and if we will ask to print the fifth element we will get the complete nested list as it is set as one element.
print (numlist[5])

#if we want to get inside the nested list we need to specify it as 2 dimentions element:
print (numlist[5][0])
print (numlist[5][1])
print (numlist[5][2])

#How to remove the last element from a list:
print ("The list is curently: " ,numlist )
numlist.pop()
print ("The list is now : " ,numlist )

numlist.pop(2)
print ("The list now after poping out the third element is: " ,numlist )

#extending an array/list
numlist.extend(numlist2)
print ("The extended list is now: " ,numlist )

#inserting to a list is done by using two values the first is the index position and the seconed is the value
numlist.insert(2,3)
print ("The extended list is now: " ,numlist )

#Creating a list as a range i.e create a list with 10 elements 0-9
range(20)
print ("The range list contains :", range(10) )

#Creating string list
stringlist = ["abc", "def", "ghi"]
print ("Following is the string list: ", stringlist)
stringlist.reverse()
print ("Following is the reversed string list: ", stringlist )  

#reversing back
stringlist.reverse()

#append to a list
stringlist.append("jkl")
print ("Following is the string list with appended string: ", stringlist)



