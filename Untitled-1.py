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

def count_chars(string, char):
    # string = string.lower()
    
    index = 0
    count = 0
    while index < len(string):
        if string[index] == char:
            count += 1
        index += 1
    return count
count_chars('HexlEt', 'e')
count_chars('HexlEt', 'E')