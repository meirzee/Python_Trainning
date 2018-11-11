#palindrom Excersice  Looping inside the string  
import sys

word = input('please insert a string: ')
word_lenght = len(word) 

for i in range(1,word_lenght// 2):
    w = word[i-1]
    r = word[word_lenght - i]
    if w != r:
        print ("not palindrom..")
        sys.exit()

print ("The string is a palindrom")
print (word, "and its reversed pattern are identical" )
sys.exit()
