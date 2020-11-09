

old_list = ['1', '2', '3', '4', '5', '6', '7']

new_list = []

# 1
for item in old_list:
    new_list.append(int(item))

print(new_list)


# 2 use map

new_list = list(map(int, old_list))
print(new_list)


# 3 use other func

def miles_to_km(num_miles):
    return num_miles * 1.6


mile_distance = [1.0, 6.5, 17.4, 2.4, 9]
km_distance = list(map(miles_to_km, mile_distance))

print(km_distance)


# 4 use lamdba

km_distance = list(map(lambda num_miles: num_miles * 1.6, mile_distance))
print(km_distance)