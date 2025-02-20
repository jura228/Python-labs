d1 = int(input("Введіть довжину першого прямокутника: "))
w1 = int(input("Введіть ширину першого прямокутника: "))
d2 = int(input("Введіть довжину другого прямокутника: "))
w2 = int(input("Введіть ширину другого прямокутника: "))

perimeter1 = 2 * (d1 + w1)
perimeter2 = 2 * (d2 + w2)

total_wire_length = perimeter1 + perimeter2

print("Необхідна довжина дроту:", total_wire_length)
