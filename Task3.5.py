number = int(input(f"Введите целое число: "))
positive = [1, 1]
negative = [1, -1]
for i in range(2, number):
    fibon = positive[i-1] + positive[i-2]
    positive.append(fibon)
    if i % 2 == 0:
        negative.append(fibon)
    else:
        negative.append(-fibon)
negative.reverse()
negative.append(0)
print(negative+positive)