import datetime
import os

login = "Alice"
password = "1235"

input_login = input("Введите логин: ")
while input_login != login:
    print("Такого пользователя нет. Попробуйте снова.")
    input_login = input("Введите логин: ")
input_password = input("Введите пароль: ")
while input_password != password:
    print("Неверный пароль!")
    input_password = input("Введите пароль: ")
print(f"Добро пожаловать, {login}!")

input_text = input("Чем я могу вам помочь?")
while input_text != "стоп":
    # print(f"Ваше сообщение: '{input_text}'")
    if input_text == "Как дела?":
        print("Хорошо, а твои?")
    elif input_text == "Какая погода сегодня?":
        print("Сегодня -4 градуса. Наденьте куртку")
    elif input_text == "инфо":
        print(f"\tlogin: {login}")
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