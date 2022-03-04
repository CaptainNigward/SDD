#v0.1
from operator import truediv
from re import search


search_array = [15, 16, 88, 99, 66, 777, 456, 852]
search_term = int(input("please enter your search number"))

# for i in search_array:
#     if search_term == i:
#         print("found!")

#v0.2
# Found = False
# for i in search_array:
#     if Found == False:
#         if search_term == i:
#             print("found!")
#             Found == True 

#v0.3

Found = False 
current_item = 0 
length_of_array = len(search_array)
while Found == False and current_item <= length_of_array:
    if search_array[current_item] == search_term: 
        Found = True 
    else:
        current_item += 1

if Found == True:
    print("found")

