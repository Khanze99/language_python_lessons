colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]  # Генерирует список кортежей, упорядоченный сначала
# по цвету, а затем по размеру
print(tshirts)


for color in colors:  # Обратите внимание, что результирующий список упорядочен так, как если бы циклы были вложены
    # именно в том порядке, в котором указаны в списковом включении
    for size in sizes:
        print((color, size))


tshirts = [(color, size) for size in sizes
                         for color in colors]  # Чтобы расположить элементы сначала по размеру, а затем по цвету,
# нужно просто поменять местами предложения for; после переноса второго предложения for на другую строку стало понятнее,
# как будет упорядочен результат
print(tshirts)