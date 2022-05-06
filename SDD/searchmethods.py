#v0.1
from operator import truediv
from re import search


# search_array = [15, 16, 88, 99, 66, 777, 456, 852]
# search_term = int(input("please enter your search number"))

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

# Found = False 
# current_item = 0 
# length_of_array = len(search_array)
# while Found == False and current_item <= length_of_array:
#     if search_array[current_item] == search_term: 
#         Found = True 
#     else:
#         current_item += 1

# if Found == True:
#     print("found")


# search_array = [1, 2, 3, 9, 11, 13, 17, 25, 57, 90]
# search_term = int(input("please enter your search number"))

# low = 0
# high = len(search_array) - 1
# mid = (high + low)//2 #interger division = cuts off the decimal
# found = False 

# print(low, mid, high)

# while found == False: 
#     if search_term == search_array[mid]: 
#         found == True 
#     elif search_term > search_array[mid]:
#         mid = (high + mid) // 2 
#     else:
#         mid = (low + mid)// 2
    
# if found == True:
#     print ("you found it")
