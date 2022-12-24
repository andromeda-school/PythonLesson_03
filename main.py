import datetime
import os
import random

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
print("\n============================")
print(f"Добро пожаловать, {login}!")
print("============================\n")

print("Чем я могу вам помочь?")
input_text = input("Введите команду: ")
while input_text != "стоп":
    if input_text == "Как дела?":
        print("У меня все хорошо!\n")
    elif input_text == "Какая погода сегодня?":
        print("Сегодня -1 градус. Наденьте куртку\n")
    elif input_text == "инфо":
        print(f"\tlogin: {login}")
        print(f"\tpassword: {password}\n")
    elif input_text == "Создай папку":
        print("Будет сделано!")
        input_text = input("как ее назвать: ")
        os.mkdir(input_text)
        print(f"Папка с именем '{input_text}' создана!\n")
    elif input_text == "Сколько время?":
        today = datetime.datetime.today()
        print("Cейчас", today.strftime("%H:%M:%S"), "\n")
    elif input_text == "Загадай цвет.":
        colors = ["Зеленый", "Синий", "Красный", "Желтый", "Белый", "Черный" ]
        print(f"Хммм... {random.choice(colors)}!\n")
    elif input_text == "Посоветуй фильм":
        print("Посмотрите 'Один дома'.")
        print("Скоро ведь новый год :)\n")
    elif input_text == "Кто ты?":
        print("Я - Ассистент-помощник. Создана на языке программирования Python.\n")
    else:
        print("Такую команду не знаю.\n")
    input_text = input("Введите новую команду: ")

print("\nХорошего дня! :)")