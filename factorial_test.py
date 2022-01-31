input_factorial = int(input("Введите число: "))
factorial_list = [f for f in range(2, input_factorial + 1)]  # разбирает число на факториал


def get(f):  # разбирает число на простые множители
    factors = list()
    list_1 = []
    for numb in f:  # перебирает факториал
        dev = 2
        while dev <= numb:
            if (numb % dev) == 0:
                factors.append(dev)
                numb = int(numb / dev)
                list_1.append(dev)
            else:
                dev += 1
    return list_1


def disassemble(list):      # разбирает полученный список в строку
    list.sort()
    value = 0
    result = ''
    for i in list:
        if i != value:
            countedvalue = list.count(i)
            if countedvalue != 1:
                result = result + str(i) + '^' + str(countedvalue) + "*"
            else:
                result = result + str(i) + "*"
        value = i

    result = result[:len(result) - 1]
    print(result)


list_2 = get(factorial_list)
disassemble(list_2)
