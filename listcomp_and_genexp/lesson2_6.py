# Порождение декартова произведения генераторным выражением

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# Генераторное выражение отдает по одному элементу за раз; список, содержащий все шесть вариаций
# футболки, не создается
