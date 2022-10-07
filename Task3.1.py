count = int(input("Введите количество элементов списка: "))
number_list = list()
number_list = [0] * count
for i in range(count):
    number_list[i] = input(f"Введите число {i+1}-й элемент списка: ")
    while not number_list[i].isdigit():
        number_list[i] = input("Вы ввели некорректное число. Повторите ввод: ")
    number_list[i] = int(number_list[i])
summa = 0
add_list = list()
for i in range(0, len(number_list), 2):
    summa += number_list[i]
    add_list.append(number_list[i])
print(f"Сумма элементов списка, стоящих на нечётных позициях: {add_list}, равна {summa}")