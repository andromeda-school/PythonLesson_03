
#
#   Создадим программу, которая
#    будет записывать наши фильмы в список
#

n = int(input("Введите количество фильмов:"))
movies_list = [] # ['Оно', 'Железный человек', 'Интерстеллар']

for i in range(n):
    movie = input("Введите фильм: ")
    movies_list.append(movie)

print(movies_list)

# давайте теперь найдем фильм в нашем списке

movie_name = input("Какой фильм найти: ")
find_key = False

for movie in movies_list:
    if movie == movie_name:
        find_key = True     # отмечаем, что нашли фильм
        break               # BREAK выгоняет нас из цикла,
                            # чтобы лишний раз не искать фильм
                            # (он ведь уже найден)
if find_key:
    print("Найдено! Фильм '", movie_name, "' есть в библиотеке.")
else:
    print("Такого фильма нет в библиотеке")
