season_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}

month = int(input("Введите порядковый номер месяца (от 1 до 12): "))

if month in sum(season_dict.values(),[]):
        for i in season_dict.items():
            if month in i[1]:
                print(i[0])
                break
else:
    print("Ты дебил? Cказано же цифру от 1 до 12")