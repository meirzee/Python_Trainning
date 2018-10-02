#How to write changing data to a file IO 
#The write command handles strings only but we still can write variables to a file (changing information)

han1 = open("meir", 'w')


prodname = "LinuxCBT"
ProductCost = 395
count = 1

# The following line will return erro: 
# han1.write(prodname,ProductCost,count)
# This is because the write function excepts only one argument and only strings so we can insert it as tuple 
# Also we need to do formating to the variables so the write function will know how to handle it - format it so it will be converted to strings
# This can be done using % as follow:
# The % operator when applied to strings performs formating
# %s - strings %d - digits/integers %f - float numbers

han1.write("%s %d %d \n\n" % (prodname,ProductCost,count) )
han1.close()
# Putting the values (prodname,ProductCost,count) in the paranthesis turns them into a tuple that way the write function receives them as one argument.
# The tuple will contain 3 variables that will be assosiated with the 3 formating types accordingly

print (open('meir', 'r').read() )


han2 = open('meir' , 'r').read()
print(han1)


