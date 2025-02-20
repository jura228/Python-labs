import math

x = float(input("Введіть значення x: "))

if x > 0:
    log_x = math.log10(x)
    cos_value = math.cos(3 * x)
    denominator = 1 + cos_value

    if denominator != 0:
        numerator = x - log_x
        expression = numerator / denominator + 1

        print(f"numerator = {numerator:.5f}, denominator = {denominator:.5f}, expression = {expression:.5f}")

        if -1 <= expression <= 1:
            y = math.acos(expression)
            print(f"y = {y:.5f}")
        else:
            print("Помилка: значення виразу виходить за межі [-1, 1], arccos неможливий.")
    else:
        print("Помилка: ділення на нуль (знаменник = 0).")
else:
    print("Помилка: x має бути більше за 0 (логарифм не визначений для x ≤ 0).")
