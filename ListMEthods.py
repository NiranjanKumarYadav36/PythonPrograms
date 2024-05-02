## Find the Sum and Average of LIST elements 

list_ = [1, 3, 4, 6, 8]


add = 0
count = 0
for number in list_:
    add = add + number
    count = count + 1
    
print("additions is", add )

count = add / count
print("average is", count )    

# additions is 22
# average is 4.4



## Search for a NAME in a LIST of names

name_list = ["niranjan", "ammar", "om"]

search_name = "ammar"

if search_name in name_list:
    print(search_name + " name found in list")
    index = name_list.index(search_name)
    print("index is", index)
    
 
# ammar name fount in list
# index is 1   



## Count the occurrences of a given string or number

number_lsit = [1, 4, 6, 1,  1, 3, 2, 3, 2, 6]

count = number_lsit.count(1)
print("occurrence is ", count)

# occurrence is  3



## Search for a given number and then remove it from the list

number_lsit = [1, 4, 6, 1,  1, 3, 2, 3, 2, 6]

search_number = 1

if search_number in number_lsit:
    print("yes")
    number_lsit.remove(search_number)

print(number_lsit)    


# yes
# [4, 6, 1, 1, 3, 2, 3, 2, 6]


## Perform sorting on a LIST

number_lsit.sort()

print("Ascending order", number_lsit)

number_lsit.sort(reverse=True)
print("Descending order", number_lsit)


# Ascending order [1, 1, 2, 2, 3, 3, 4, 6, 6]
# Descending order [6, 6, 4, 3, 3, 2, 2, 1, 1]

