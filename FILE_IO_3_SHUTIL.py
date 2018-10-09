#file io 3 - shutil is a utility for handling files
import shutil

SHUTIL_FUNCTION = dir(shutil)
print ("following are the SHUTIL functions: \n ", )
for i in SHUTIL_FUNCTION:
    print (i)

s = shutil  # creating a short name for the shutil for convinient purpose.

#copy file source to target
s.copy("datafile1","datafile2" )

#copy with preserving the date time stamp ( like cp -p file_name)
s.copy2("datafile1","datafile3")

# move fille function works for directories too.
s.move("datafile1" , "data_moved")

# Copy tree of directory recursivly
# s.copytree ("source", "target")  # target should not exist other wise error will be return it is not overriding the tree
# there is a third argument to this function that treats symbolic links
# s.copytree ("source", "target", 0 ) 
# 0 - will copy the file itself
# 1 - will copy the link

# How to remove dir:
# s.rmtree(sourcedir , ignore_errors=True)


