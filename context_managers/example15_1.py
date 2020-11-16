
with open('context_managers/README.md') as fp:  # Имя fp связано с откртым файлом, потому что метод __enter__
    # объекта-файла возвращает self
    src = fp.read(60)  # Читаем данные

print(len(src))
print(src)  # Мы так же можем прочитать из переменной данные, которые записаны в памяти

print(fp)  # Переменная fp все еще доступна
print(fp.closed, fp.encoding)  # Мы можем прочитать атрибуты объекта
print(fp.read())  # Но выполнить заново операцию ввода и вывода не можем, т.к. уже был
# вызван метод TextIOWrapper.__exit__
