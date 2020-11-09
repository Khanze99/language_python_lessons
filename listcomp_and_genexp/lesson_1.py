
# ord() возвращает числовое представление для указанного символа.

x = 'ABC'
dummy = [ord(x) for x in x]  # Списковые включения имеют свои локальные области

print(x)  # значение x сохранено
print(dummy)  # Списковое включение порождает ожидаемый список
