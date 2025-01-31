x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))

results = [x + y, x - y, x * y, x / y if y != 0 else "Ділення на нуль неможливе", x // y if y != 0 else "Цілочисельне ділення на нуль неможливе", x % y if y != 0 else "Остача від ділення на нуль неможлива", x ** y]

print("Список результатів:", results)

new_list = [results[1], results[4]]
print("Новий список:", new_list)
