N = int(input("Введіть кількість друзів: "))
m = float(input("Введіть суму рахунку (грн): "))

tip = m * 0.15

total_amount = m + tip  

if N > 0:
    amount_per_friend = total_amount / N
    print(f"Кожен друг має заплатити: {amount_per_friend:.2f} грн")
else:
    print("Кількість друзів має бути більше 0")
