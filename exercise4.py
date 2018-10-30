
get_num = int(input("please select a number: "))
print(get_num)

get_num_r = range (1, (get_num + 1) )
list_of_numbers= []

for i in get_num_r:
    if get_num % i == 0:
        list_of_numbers.append(i)

print ("following are the numbers that can devide " , get_num, ":" ,list_of_numbers)
        


