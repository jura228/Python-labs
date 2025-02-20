numbers = list(range(0, 57, 2))
print("Список:", numbers)

doubled_numbers = [num * 2 for num in numbers]
print("Список після збільшення в 2 рази:", doubled_numbers)

stats = {
    "Сума": sum(doubled_numbers),
    "Мінімальний елемент": min(doubled_numbers),
    "Максимальний елемент": max(doubled_numbers)
}
print("Статистика:", stats)

tuple_numbers = tuple(doubled_numbers)
string_numbers = " ".join(map(str, doubled_numbers))

print("Кортеж:", tuple_numbers)
print("Тип кортежу:", type(tuple_numbers))
print("Рядок:", string_numbers)
print("Тип рядка:", type(string_numbers))
