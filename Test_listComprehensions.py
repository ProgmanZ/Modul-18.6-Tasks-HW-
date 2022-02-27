# list_a = [1, 2, 3, 4, 5, 6, 7]
#
# list_b = [elem_list_a for elem_list_a in list_a]
#
# print(list_b)

black_list = [
    [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [11, 12, 13]], [[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [11, 12, 13]]],
    [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [11, 12, 13]], [[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [11, 12, 13]]]]

# list_b  - вложенный список
# list_a  - первый список
# element - значение, которое необходимо вывести

# list_c = [element for list_b in list_a for element in list_b]


# list_g = [element for list_b in list_a for element in list_a]


list_f = [element for blue_list in black_list for red_list in blue_list for green_list in red_list for element in green_list]

print(list_f)
print(len(list_f))
