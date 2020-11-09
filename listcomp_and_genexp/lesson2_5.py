# Инициализация кортежа и массива с помощью генераторного выражения

symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))  # Если генераторное выражение - единственный аргумент функции,
# то дублировать круглые скобки необязательно


import array
print(array.array('I', (ord(symbol) for symbol in symbols)))
# Конструктор массива принимает два аргумента, поэтому скобки вокруг генераторного выражения обязательны. Первый
# аргумент конструктора array определяет тип хранения чисел в массив