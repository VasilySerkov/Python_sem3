count = int(input("Введите количество элементов списка: "))
number_list = list()
number_list = [0] * count
for i in range(count):
    number_list[i] = input(f"Введите число {i+1}-й элемент списка: ")
    while not number_list[i].isdigit():
        number_list[i] = input("Вы ввели некорректное число. Повторите ввод: ")
    number_list[i] = int(number_list[i])
pair_mltpl = list()
for i in range(len(number_list)//2 + len(number_list)%2):
    pair_mltpl.append(number_list[i] * number_list[-i-1])
print(f"Произведения пар элементов: {pair_mltpl}")