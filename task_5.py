my_list = [9, 7, 5, 5, 5, 4, 3, 3, 2, 1]
person_number = int(input("Введите число от 0 до 9: "))
i = 0
for n in my_list:
    if person_number <= n:
        i += 1
    else:
        break
my_list.insert(i, person_number)
print(my_list) #
