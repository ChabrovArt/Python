my_list = [17, 48, 9, 3, 84, 38, 67, 3, 58, 87, 45]
more_than = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_than)