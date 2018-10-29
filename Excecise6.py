#Execrcise6
#Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)


StringOne = input("\nPlease insert a string:")

print("You chossed string: ", StringOne)

String_len = len(StringOne)
print (String_len)

s2 = StringOne[String_len:0]
print("from end to start: ", s2 )

