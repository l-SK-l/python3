# def truncate(text, length):
#     return text[:length] + '...'
# print(truncate('Hello',3))

# def truncate2(text, length):
#     result = f'{text[0:length]}...'
#     return result
# print(truncate2('Hello',4))

# def get_hidden_card(card_number, secret_len=4):
#     hide_card_number = card_number[-4:]
#     return f'{"*" * secret_len}{hide_card_number}'
# print(get_hidden_card('2034399002125581', 3))

# def trim_and_repeat(text, offset=0, repetitions=1):
#     cut_text = text[offset:]
#     cut_text = cut_text * repetitions
#     return cut_text
# print(trim_and_repeat('python', 3, 2))

# def trim_and_repeat(text, offset=0, repetitions=1):
#     return f'{text[offset:] * repetitions}'
# print(trim_and_repeat('python', 3, 2))

# def is_international_phone(number):
#     is_international = number[0] == '+'
#     return is_international
# print(is_international_phone('+89602223423'))

# def is_leap_year(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
# print(is_leap_year(2000))

# def is_palindrome(word):
#     word = word.lower()
#     return word[0::] == word[::-1] #можно не читать с правой стороны
# print(is_palindrome('elle')) 
# def is_not_palindrome(word):
#     word = word.lower()
#     return word[0::] != word[::-1]
# print(is_palindrome('elle'))

# def string_or_not(value):
#     value = isinstance(value, str) 
#     return value != 0 and'yes' or 'no'
# print(string_or_not(None))
# def string_or_not(value): #проще
#     return isinstance(value, str) and 'yes' or 'no'
# print(string_or_not("None"))

# def guess_number(number):
#     if number == 42:
#         return 'You win!'
#     return 'Try again!'
# print(guess_number(42))

# def normalize_url(url):
#     is_colon = url[5]
#     if is_colon == ':':
#         return url
#     is_colon = url[4]
#     if is_colon == ':':
#         url = url[7:]
#         return f'https://{url}'
#     else:
#         return f'https://{url}'
# print(normalize_url('yta.ru'))

# def normalize_url(url):
#     prefix = 'https://'
#     if url[:8] == prefix:
#         return url
#     else:
#         if url[:7] == 'http://':
#             return prefix + url[7:]
#         else:
#             return prefix + url

# def who_is_this_house_to_starks(famely):
#     if famely == 'Karstark' or famely == 'Tully':
#         return 'friend'
#     elif famely == 'Lannister' or famely == 'Frey':
#         return 'enemy'
#     else:
#         return 'neutral'
# print(who_is_this_house_to_starks('Frey'))

# def flip_flop(string):
#     return 'flop' if string == 'flip' else 'flip'
# print(flip_flop('flop'))

# Модифицируйте функцию print_numbers() так, чтобы она выводила числа в обратном порядке. 
# Для этого нужно идти от верхней границы к нижней. 
# То есть счётчик должен быть инициализирован максимальным значением, 
# а в теле цикла его нужно уменьшать до нижней границы.

# def print_numbers(number):
#     i = number
#     while i > 0:
#         print(i)
#         i -= 1
#     print('ended')
# print(print_numbers(4))

# Реализуйте функцию multiply_numbers_from_range(), которая перемножает числа 
# в указанном диапазоне включая границы диапазона

# def multiply_numbers_from_range(first_number, second_number):
#     i = first_number
#     result = 1
#     while i <= second_number:
#         result = result * i
#         i = i + 1
#     return result
# print(multiply_numbers_from_range(2, 3))

# Реализуйте функцию join_numbers_from_range(), 
# которая объединяет все числа из диапазона в строку
# def join_numbers_from_range(start, end):
#     result = ''
#     i = start
#     while i <= end:
#         result = str(result) + str(i)
#         i += 1
#     return result
# print(join_numbers_from_range(5, 10))

# Реализуйте функцию print_reversed_word_by_symbol(), 
# которая печатает переданное слово посимвольно, 
# как в примере из теории, но делает это в обратном порядке
# word = 'Hexlet'
# def print_reversed_word_by_symbol(word):
#     i = 0
#     index = -1
#     while i < len(word):
#         print(word[index])
#         i += 1
#         index -= 1
# print_reversed_word_by_symbol(word)
# # OR
# def print_reversed_word_by_symbol(word):
#     i = len(word) - 1
#     while i >= 0:
#         print(word[i])
#         i = i - 1

# Функция из теории учитывает регистр букв. 
# То есть A и a с её точки зрения разные символы. 
# Реализуйте вариант этой же функции, так чтобы регистр букв был не важен:

# def count_chars(string, char):
#     index = 0
#     count = 0
#     while index < len(string):
#         if string[index].lower() == char.lower():
#             count += 1
#         index += 1
#     return count
# print(count_chars('HexlEt', 'e'))
# print(count_chars('HexlEt', 'E'))

# Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины. 
# Она принимает на вход два аргумента: строку и длину, и возвращает подстроку, 
# начиная с первого символа

# string = 'If I look back I am lost'
# def my_substr(string, length):
#     index = 0
#     substr = ''
#     while index < length:
#         substr = substr + string[index]
#         index += 1
#     return substr
# print(my_substr(string, 7))


# Реализуйте функцию-предикат is_arguments_for_substr_correct(), 
# которая принимает три аргумента:
#     строку;
#     индекс, с которого начинать извлечение;
#     длину извлекаемой подстроки.
# Функция возвращает False, если хотя бы одно из условий истинно:
#     Отрицательная длина извлекаемой подстроки.
#     Отрицательный заданный индекс.
#     Заданный индекс выходит за границу всей строки.
#     Длина подстроки в сумме с заданным индексом выходит за границу всей строки.
# В ином случае функция возвращает True.

# string = 'Sansa Stark'
# def is_arguments_for_substr_correct(string, index, length):
#     if length < 0:
#         return False
#     elif index < 0:
#         return False
#     elif index > len(string) - 1:
#         return False
#     elif length + length > len(string):
#         return False
#     return True
# print(is_arguments_for_substr_correct(string, 2, -3))   # => False
# print(is_arguments_for_substr_correct(string, -1, 3))   # => False
# print(is_arguments_for_substr_correct(string, 4, 100))  # => False
# print(is_arguments_for_substr_correct(string, 10, 10))  # => False
# print(is_arguments_for_substr_correct(string, 11, 1))   # => False
# print(is_arguments_for_substr_correct(string, 3, 3))    # => True
# print(is_arguments_for_substr_correct(string, 0, 5))    # => True

# Реализуйте функцию filter_string(), принимающую на вход строку и символ, 
# и возвращающую новую строку, в которой удален переданный символ во всех его позициях.

# text = 'If I look back I am lost'
# def filter_string(string, char):
#     i = 0
#     result = ""
#     while i < len(string):
#         if string[i] == char:
#              result += ""
#         elif string[i] != char:
#             result += string[i]
#         i += 1
#     return result
# print(filter_string(text, 'I'))
# print(filter_string(text, 'o'))

# # OR

# def filter_string(text, char):
#     index = 0
#     result = ''
#     while index < len(text):
#         current_char = text[index]
#         if current_char != char:
#             result = f'{result}{current_char}'
#         index += 1
#     return result
# print(filter_string(text, 'I'))
# print(filter_string(text, 'o'))

# Реализуйте функцию is_contains_char(), которая проверяет с учётом регистра, 
# содержит ли строка указанную букву. Функция принимает два параметра:
#     Строка
#     Буква для поиска

# def is_contains_char(string, char):
#     i = 0
#     while i < len(string):
#         if string[i] == char:
#             return True
#         i += 1
#     return False
# print(is_contains_char('Hexlet', 'H'))  # => True
# print(is_contains_char('Hexlet', 'h'))  # => False
# print(is_contains_char('Awesomeness', 'm'))  # => True
# print(is_contains_char('Awesomeness', 'd'))  # => False


# В одном из предыдущих уроков мы уже написали функцию filter_string(). 
# Напомним, она принимает на вход строку и символ и возвращает новую строку, 
# в которой удалён переданный символ во всех его позициях. 
# На этот раз реализуйте эту функцию с помощью цикла for. 
# Дополнительное условие: регистр исключаемого символа не имеет значения.

# text = 'If I look forward I win'
# def filter_string(text, char):
#     result = ''
#     for corrent_text in text:
#         if corrent_text.upper() != char.upper():
#             result = f'{result}{corrent_text}'
#     return result
# print(filter_string(text, 'I'))  # 'f  look forward  wn'
# print(filter_string(text, 'o'))  # 'If I lk frward I win'


# Выведите все элементы списка с четными индексами 
# (то есть A[0], A[2], A[4], ...). 

# a = input().split()
# for i in range(0, len(a), 2):
#     print(a[i], end = ' ')


# Выведите все четные элементы списка. При этом используйте цикл for, 
# перебирающий элементы списка, а не их индексы! 

# a = input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])
# # print(a)
# for i in a:
#     if i % 2 == 0:
#         print(i, end=' ')

# # OR

# s = input()
# a = [int(s) for s in s.split()]
# for i in a:
#     if int(i) % 2 == 0:
#        print(i, end=' ')


# Дан список чисел. Выведите все элементы списка, 
# которые больше предыдущего элемента. 

# s = input()
# z = 0
# a = [int(s) for s in s.split()]
# # print(a)
# for i in a[1:]:
#     if i > a[z]:
#         print(i, end = ' ')
#     z += 1

# # OR

# a = [int(i) for i in input().split()]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])

# Дан список чисел. Если в нем есть два соседних элемента одного знака, 
# выведите эти числа. Если соседних элементов одного знака нет — 
# не выводите ничего. Если таких пар соседей несколько — 
# выведите первую пару. 

# a = [int(i) for i in input().split()]
# x = 0
# for i in a[1:]:
#     if (a[x] < 0 and i < 0) == True:
#         print(a[x], i)
#         break
#     elif (a[x] > 0 and i > 0) == True:
#         print(a[x], i)
#         break
#     x += 1

# # OR

# a = [int(i) for i in input().split()]
# for i in range(1, len(a)):
#     if a[i - 1] * a[i] > 0:
#         print(a[i - 1], a[i])
#         break


# Дан список, упорядоченный по неубыванию элементов в нем. 
# Определите, сколько в нем различных элементов. 

# a = [int(i) for i in input().split()]
# new_list = []
# count = 0
# for i in a:
#     if i not in new_list:
#         count += 1
#         new_list.append(i)
# print(count)


# Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв
#  и возвращает его же, меняя первую букву на большую.
# Например, print(capitalize('word')) должно печатать слово Word. 
# Слов может быть несколько через пробел. Слова состоят из маленьких латинских букв.

# def capitalize(x):
#     result = ""
#     lst = x.split()
#     for i in lst:
#         first_letter = i[0].upper()
#         other_letter = i[1:]
#         result = result + first_letter + other_letter + " "
#     return result

# print(capitalize(input()))


# В единственной строке записан текст. 
# Для каждого слова из данного текста подсчитайте, 
# сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.

# counter = {}  # создаём пустой словарь
# for word in input().split():  # превращаем строку в отдельные значения, разделитель пробел
#     counter[word] = counter.get(word, 0) + 1  # добавляем ключи в ловарь с цифрой 1 в значении при каждом добавлении ключа
#     print(counter[word] - 1, end=' ')


# В первой строке дано количество записей. 
# Далее, каждая запись содержит фамилию кандидата и число голосов, 
# отданных за него в одном из штатов. 
# Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов. 
# Участников нужно выводить в алфавитном порядке.

# num_votes = {}
# for _ in range(int(input())):  # Указываем число строк
#     candidate, votes = input().split()  # разбираем строки на 2 переменных, пример данных 'Obama 9'
#     num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)  #Добавляем данный в словарь складывая голова отдельно т.к. есть несколько строк с одним ключём и разными значениями

# print(num_votes)  # выводим отсортированный словарь
# for candidate, votes in sorted(num_votes.items()):  # сортируем словарь по ключу(items) и выводим пары ключ:значение по отдельности
#     print(candidate, votes)


