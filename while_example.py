import time

# Пример бесконечного цикла

while True:
    time.sleep(0.3)
    print("БЕСКОНЕЧНОСТЬ")

#
#   Создадим программу по учету машин
#    Пусть она добавляет, удаляет
#     и показывает список машин
#

cars_list = ["BMW", "Audi", "Opel", "Mers"]
command = input("Введите действие: ")

while command != "СТОП":  # пока команда не "стоп"
    if command == "Добавить":
        cars_list.append(input("Введите машину для добавления: "))
        print("Добавлено!")
    elif command == "Все машины":
        print(cars_list)
    elif command == "Удалить":
        cars_list.remove(input("Введите машину для удаления: "))
        print("Удалено.")
    else:
        print("Такой комманды неизвестно")
    command = input("Введите следующее действие: ")

