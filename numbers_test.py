numbers_value = {
    'ноль': 0, 'нуля': 0, 'нулю': 0, 'нулём': 0, 'нуле': 0, 'один': 1, 'единица': 1, 'одного': 1, 'одному': 1,
    'одна': 1, 'первый': 1, 'первого': 1, 'первому': 1, 'первым': 1, 'первом': 1, 'два': 2, 'двух': 2, 'двумя': 2,
    'две': 2, 'второй': 2, 'второго': 2, 'второму': 2, 'вторым': 2, 'втором': 2, 'три': 3, 'трёх': 3, 'трём': 3,
    'тремя': 3, 'четыре': 4, 'четырёх': 4, 'четырём': 4, 'четырьмя': 4, 'пять': 5, 'пяти': 5, 'пятью': 5, 'шесть': 6,
    'шести': 6, 'шестью': 6, 'семь': 7, 'семи': 7, 'восемь': 8, 'восеми': 8, 'восьмью': 8, 'девять': 9, 'девяти': 9,
    'девятью': 9, 'десять': 10, 'десяти': 10, 'десятью': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
    'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
    'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
    'девяносто': 90, 'сто': 100, "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500, "шестьсот": 600,
    "семьсот": 700, "восемьсот": 800, "девятьсот": 900, 'тысяча': 1000, 'тысячи': 1000, 'тысяче': 1000, 'тысячу': 1000,
    'тысячей': 1000, 'тысяч': 1000, 'миллион': 1000000
}


def number_formation(
        number_words):  # распознает количество символов и в зависимости от этого выполняет сложение или умножение и
    list = []  # переводит в числовой формат
    for number_word in number_words:
        list.append(numbers_value[number_word])
    if len(list) == 4:
        return (list[0] * list[1]) + list[2] + list[3]
    elif len(list) == 3:
        return list[0] + list[1] + list[2]
    elif len(list) == 2:
        return list[0] + list[1]
    else:
        return list[0]


def word_to_num(number_sentence):  # основная функция
    if type(number_sentence) is not str:
        raise ValueError(
            "Неверный тип данных! Пожалуйста, введите верный формат (Пример семьсот восемьдесят три тысячи девятьсот девятнадцать)")

    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower()  # Убираем заглавные буквы

    if number_sentence.isdigit():  # Возвращает значение если пользователь ввел цифру не прописью
        return int(number_sentence)

    split_words = number_sentence.strip().split()  # Удаляет лишнее пространство и разделяет на слова

    clean_numbers = []

    for word in split_words:
        if word in numbers_value:
            clean_numbers.append(word)

    # Ошибка, если пользователь ввел неверные символы!
    if len(clean_numbers) == 0:
        raise ValueError(
            "Не найдены нужные слова! Пожалуйста, введите верный формат (пример: семьсот восемьдесят три тысячи девятьсот девятнадцать)")

    # Ошибка если пользователь дважды ввел - миллиона,тысячи,сотни или десятки
    if clean_numbers.count('тысяча') > 1 or clean_numbers.count('тысячи') > 1 or clean_numbers.count(
            'тысяч') > 1 or clean_numbers.count('миллион') > 1:
        raise ValueError(
            "Лишнее слово ! Пожалуйста, введите верный формат (пример: семьсот восемьдесят три тысячи девятьсот девятнадцать)")

    if 'миллион' in clean_numbers:  # Поиск миллионов
        million_index = clean_numbers.index('миллион')
    else:
        million_index = -1

    if 'тысяч' in clean_numbers:  # Поиск тысяч
        thousand_index = clean_numbers.index('тысяч')
    elif 'тысячи' in clean_numbers:
        thousand_index = clean_numbers.index('тысячи')
    elif 'тысяча' in clean_numbers:
        thousand_index = clean_numbers.index('тысяча')
    elif 'тысяче' in clean_numbers:
        thousand_index = clean_numbers.index('тысяче')
    elif 'тысячу' in clean_numbers:
        thousand_index = clean_numbers.index('тысячу')
    elif 'тысячей' in clean_numbers:
        thousand_index = clean_numbers.index('тысячей')
    else:
        thousand_index = -1

    if (thousand_index > -1 and (thousand_index < million_index)) and (million_index > -1):
        raise ValueError(
            "Неверный вормат записи чисел! Пожалуйста, введите верный формат (пример: семьсот восемьдесят три тысячи девятьсот девятнадцать)")

    total_sum = 0  # сохраняем результат который будем возвращать

    if len(clean_numbers) > 0:  # Ищем по разделению миллион/тысяча и в зависимости от введенных данных вызываем
        # функцию переводящую в из буквенного формата в числовой
        if len(clean_numbers) == 1:
            total_sum += numbers_value[clean_numbers[0]]

        else:
            if million_index > -1:
                million_multiplier = number_formation(clean_numbers[0:million_index])
                total_sum += million_multiplier * 1000000

            if thousand_index > -1:
                if million_index > -1:
                    thousand_multiplier = number_formation(clean_numbers[million_index + 1:thousand_index])
                elif thousand_index == 0:
                    thousand_multiplier = 1

                else:
                    thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
                total_sum += thousand_multiplier * 1000

            if thousand_index > -1 and thousand_index == len(clean_numbers) - 1:
                hundreds = 0
            elif thousand_index > -1 and thousand_index != len(clean_numbers) - 1:
                hundreds = number_formation(clean_numbers[thousand_index + 1:])
            elif million_index > -1 and million_index != len(clean_numbers) - 1:
                hundreds = number_formation(clean_numbers[million_index + 1:])
            elif thousand_index == -1 and million_index == -1:
                hundreds = number_formation(clean_numbers)
            else:
                hundreds = 0
            total_sum += hundreds

    return total_sum
