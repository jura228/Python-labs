num = int(input("Введіть тризначне число: "))

if 100 <= num <= 999:
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    
    digit_sum = hundreds + tens + ones
    print(f"Сума цифр числа: {digit_sum}")

    swapped1 = tens * 100 + hundreds * 10 + ones
    print(f"Число з поміняними сотнями і десятками: {swapped1}")

    swapped2 = ones * 100 + tens * 10 + hundreds
    print(f"Число з поміняними одиницями і сотнями: {swapped2}")
else:
    print("Введене число не є тризначним!")
