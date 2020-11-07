squeares = [i * i for i in range(10)]
print(squeares)


sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)


sentence = 'The rocket, who was named Ted, came back' \
           'from Mars because he missed his friends.'


def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

# str.isalpha() - Возвращает флаг, указывающий на то, содержит ли строка только буквы


consonants = [i for i in sentence if is_consonant(i)]
print(consonants)


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)


def get_price(price):
    return price if price > 0 else 0


prices = [get_price(i) for i in original_prices]
print(prices)


