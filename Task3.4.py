deci_number = int(input(f"Введите целое десятичное число: "))
remainder = deci_number
binary_number = ""
while remainder > 0:
    binary_number = str(remainder % 2) + binary_number
    remainder //= 2
print(f"Двоичное представление числа: {binary_number}")