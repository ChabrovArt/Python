def F(f_1, f_2):
    try:
        f_1, f_2 = int(f_1), int(f_2)
        F_num = f_1 / f_2
    except ValueError:
        return "Ошибка значения"
    except ZeroDivisionError:
        return "Деление на ноль, не надо так"
    return round(F_num, 7)

print(F(input("Введите первое число - "), input("Введите второе - ")))