from collections import defaultdict

dnh = defaultdict(list)

with open('input.txt', mode='r') as data_file:
    for line in data_file:
        name, hours = line.split(maxsplit=1)
        hours = [int(hour) for hour in hours.strip().split(',')]
        dnh.setdefault(name, []).extend(hours)

for item in dnh:
    print('{}: {}; sum: {}'.format(item, ','.join(str(hour) for hour in dnh[item]), sum(dnh[item])))


dict_names_hours = {}
with open('input.txt', mode='r') as data_file:
    for line in data_file:
        name, hours = line.split(maxsplit=1)
        hours = [int(hour.strip()) for hour in hours.strip().split(',')]
        if name in dict_names_hours:
            dict_names_hours[name]['hours'].extend(hours)
            dict_names_hours[name]['sum'] += sum(hours)
            continue

        dict_names_hours[name] = {'hours': [*hours], 'sum': sum(hours)}

for name in dict_names_hours:
    print('{}: {}; sum: {}'.format(
        name,
        ','.join(str(hour) for hour in dict_names_hours[name]['hours']),
        dict_names_hours[name]['sum']))
