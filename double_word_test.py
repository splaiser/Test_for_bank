alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
example_list = list(input('Введите символы: '))
result_list = []


def get():
    count = len(example_list)
    for numb_1 in range(0, count - 1):
        numb_count_1 = example_list.count(example_list[numb_1])
        if numb_count_1 > 1:
            numb_2 = example_list.index(example_list[numb_1], numb_1 + 1)
            matches(numb_1, numb_2)
            get()
            break


def matches(i, j):
    index = 0
    for word in alphabet:
        if example_list[i] != word:
            index += 1
        elif example_list[i] == word:
            example_list.append(alphabet[index + 1])
            if i > j:
                example_list.pop(i)
                example_list.pop(j)
            else:
                example_list.pop(j)
                example_list.pop(i)

            break


get()
print(example_list)
