pogovorka = input("Напишите свою любимую поговорку без знаков препинания: ").split()

for i, word in enumerate(pogovorka, 1):
    print(f"{i}. {word[:10]}")