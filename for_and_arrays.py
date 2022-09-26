
#
# Урок №3. Циклы for и while,
#                   а еще списки.
#

# Цикл for
for i in range(10):
    print(i)

# Еще пример
for i in range(1, 11):
    print("Цикл №", i, ". ", 2 ** i)

# Программа, которая выводит ВСЕ числа от 1 до 100
#   КОТОРЫЕ делятся на 17 без остатка
#       остальные не выводить

for i in range(1, 101):
    if (i % 17 == 0):
        print(i)

# Список чисел
arr = [0, 3, 12, 2, 5]
print(arr)
print(min(arr))
print(max(arr))
print(sorted(arr))

# Попробуем найти общие элементы в 2 списках

arr = [1, 42, 13, 433, 5, 6]
arr2 = [-4, 13, 41, 65, 5, 14, 876, 0]

for i in range(len(arr)):
    for j in range(len(arr2)):
        if arr[i] == arr2[j]:
            print("Совпадение нашлось - ", arr[i])

#
#   Еще немного примеров цикла for
#

names = ["Anton", "Vlad", "Stepan"]
for name in names:
    print(name)

for i in range(len(arr)):
    print(arr[i])

#
# А есть и двумерные списки.
# Это списки, содержащие списки.
#

arr = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

for in_arr in arr:
    for a in in_arr:
        print(a, end=" ")
    print(end="\n")


