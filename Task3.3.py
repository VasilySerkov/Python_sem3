count = int(input("Введите количество элементов списка: "))
number_list = list()
number_list = [0] * count
for i in range(count):
    while True:
        try:
            number_list[i] = float(input(f"Введите вещественное число {i+1}-й элемент списка: "))
        except ValueError:
            number_list[i] = input("Вы ввели некорректное число. Повторите ввод: ")
        else:
            break
mminimum = number_list[0] - int(number_list[0])
mmaximum = number_list[0] - int(number_list[0])
for i in range(len(number_list)):
    if (number_list[i] - int(number_list[i])) < mminimum:
        minimum = (number_list[i] - int(number_list[i]))
    if (number_list[i] - int(number_list[i])) > mmaximum:
        maximum = (number_list[i] - int(number_list[i]))
print(f"Разница между максимальным и минимальным значением дробной части равна: {round(maximum - minimum, 2)}")