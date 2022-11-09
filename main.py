import datetime
import os

name = input("Введите имя: ")
# age = int(input("Введите возраст: "))

n = "Alice"
p = "1235"

if name == n:
    password = input("Введите пароль: ")
    if password == p:
        print(f"Привет, {name}!")
        input_text = input("Чем могу помочь?: ")
        while input_text != "стоп":
            # print(f"Ваше сообщение: '{input_text}'")
            if input_text == "Как дела?":
                print("Хорошо, а твои?")
            elif input_text == "Какая погода сегодня?":
                print("Сегодня -4 градуса. Наденьте куртку")
            elif input_text == "инфо":
                print(f"\tlogin: {name}")
                print(f"\tpassword: {password}")
            elif input_text == "Создай папку":
                print("Будет сделано!")
                input_text = input("как ее назвать: ")
                os.mkdir(input_text)
            elif input_text == "Сколько время?":
                today = datetime.datetime.today()
                print("Cейчас", today.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                print("Такую команду не знаю")
            input_text = input("Введите новое сообщение: ")
    else:
        print("Неверный пароль")
else:
    print("Такого логина нет")


