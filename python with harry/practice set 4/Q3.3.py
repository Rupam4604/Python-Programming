# Convert the tuple to a list, change its first element to 50 , and convert it back
# to a tuple.

coordinate = (10, 20)

coordinate_list = list(coordinate)

coordinate_list[0] = 50

coordinate = tuple(coordinate_list)

print(coordinate)