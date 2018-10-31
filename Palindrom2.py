#palindrom Excersice  Looping inside the string  
import sys

word = input('please insert a string: ')
reversedword = reversed(word)
word_lenght = len(word)
word_iter = word_lenght // 2
count = 0
print ("word lenght is: ", word_lenght)

for i in word:
    w = i
    r = word[word_lenght - 1]
    word_lenght = word_lenght - 1
    count = count + 1
    if w == r:
        pass
    else:
        print ("not palindrom..")
        sys.exit()
    if (count > word_iter):
        print ("The string is a palindrom")
        print (word, "and its reversed pattern are identical" )
        sys.exit()
