def personal_info(**kwargs):
    return " ".join(kwargs.values())

print(personal_info(name=input("Введите свое имя: "), surname=input("Введите свою фамилию: "), birthday=input(
"Введите дату своего рождения в формате дд.мм.гг: "), city=input("Введите свой город: "), email=input("Введите свой "
                                                                                                      "email: "),
                    phone_number=input("Введите свой номер телефона: ")))