#globbing module for searching files and manipulating data system
#by default it uses the current directory but we can give it a specific path too

import glob

#searching for files on the current directory with .py extension this will return a list
search1 = glob.glob('*.py')
#print (search1)

for i in search1:
    print (i)

#we can count the number of items on the list in oeder to see how many files do we have:
print ("\n" , len(search1), "python files were found\n")

query1 = input("Please enter file or directory name you are lookig for:")
search2 = glob.glob(query1) # This will pass the user query to the glob function to search and return the results into search2 variable

if search2:
    for i in search2:
        print (i)
        print ("\nYour search contains, " , len(search2), "resaults!")
else:
    print("Sorry No match..")