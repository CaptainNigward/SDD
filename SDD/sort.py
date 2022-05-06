def bubble_sort(list):
    counter = 0
    sorted = False
    while counter < len(list) -1:
        if list[counter] > list[counter+1]:
            temp = list[counter +1 ]
            list[counter + 1 ] = list [counter]
            list [counter] = temp 
        counter = counter -1 

bubble_sort([2, 3, 5, 8, 9, 6, 4, 12, 78, 65, 98, 14])

