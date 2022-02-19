def my_pow_func(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a float number and a negative power"
    return res

print(my_pow_func(2.4, -4))