My_list = [1, 4.5, (5, 34), {3: 45, 4: "a"}, frozenset(), "sohard", True, None, range(5), [3, -3]]

for i, item in enumerate(My_list, 1):
    print(f"{i}) {item} - {type(item)}") 
