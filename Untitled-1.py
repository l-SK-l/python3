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


# a = float(input(f'Enter a nomber: '))
# a = round(a, 2)
# print(f'{a} rounded to 2 decimal places is {a}')

# a = int(input(f'Enter a nomber: '))
# b = abs(a)
# print(f'The absolute value of {a} is {b}')

# a = float(input(f'Enter a nomber: '))
# b = float(input(f'Enter another nomber: '))
# if (a - b) % 1 == 0:
#     c = True
# else:
#     c = False
# print(f'The difference between {a} and {b} is an integer? {c}!')

# a = 3 ** 0.125
# print(f'{a:.3f}')  # 1.147
# b = 150000
# print(f'${b:,.2f}')  # $150,000.00
# c = 2/10
# print(f'{c:.0%}')  # 20%

# def cube(x):
#     return x ** 3
# print(cube(2))

# def greet(name):
#     print(f'Hello {name}'!)
# greet('Harry')

# for x in range(2,11):
#     print(x)

# i = 2
# while i < 11:
#     print(i)
#     i += 1

# def doubles(number):
#     return number * 2
# y = 2
# for x in range(3):
#     print(doubles(y))
#     y += y

# def add_underscores(word):
#     new_word = "_"
#     for i in range(len(word)):
#         new_word = new_word + word[i] + "_"
#     return new_word
# phrase = "hello"
# print(add_underscores(phrase))

# word = input(f'Введите слово: ')
# if len(word) == 5:
#     print('Длина ввода составляет 5 символов')
# elif len(word) > 5:
#     print('Длина ввода больше 5 символов')
# else:
#     print('Длина ввода меньше 5 символов')

# while True:
#   data = input("Введите данные (для выхода введите 'q' или 'Q'): ")
#   if data.lower() == "q":
#     break
#   # Выполняем какие-то действия с введенными данными
#   print("Вы ввели:", data)
# print("Программа завершена.")

# for i in range(51):
#     if i % 3 == 0:
#         continue
#     print(i)

# try:
#     number = int(input(f'Введите целое число: '))
# except ValueError:
#     print('Try again')
# print(number)

# string = input(f'Введите строку: ')
# while True:
#     try:
#         number = int(input(f'Какой индекс необходимо вывести в консоль?: '))
#         print(string[number])
#     except ValueError:
#         print('Это не число, попробуйте ещё раз')
#         continue
#     except IndexError:
#         print('Индекс выходит за границу массива, попробуйте ещё раз')
#         continue
#     break

# def roll():
#     import random
#     return random.randint(1, 6)
# print(roll())

# import random
# mean = 0
# for i in range(10000):
#     mean += random.randint(1, 6)
# mean = mean / 10000
# print(f'Среднее значение из 10000 бросков: {mean:.2f}')

# cardinal_numbers = ("first", "second", "third")
# print(cardinal_numbers[1])
# position1, position2, position3 = cardinal_numbers
# print(position3)
# my_name = tuple("sergei")
# print(my_name)
# print("x" in my_name)
# new_tuple = my_name[1:]
# print(new_tuple)

# food = ["rice", "beans"]
# print(food)
# food.append("broccoli")
# print(food)
# food.extend(["bread", "pizza"])
# print(food)
# print(food[0:2])
# print(food[-1])
# breakfast = "eggs,fruit,orangejuice".split(',')
# print(breakfast)
# print(len(breakfast))
# lengths = [len(i) for i in breakfast]
# print(lengths)

# data = ((1,2), (3,4))
# print(data)
# for i in data:
#     count_list = 1
#     print(f'Row {count_list} sum: {sum(i)}')
#     count_list += 1

# numbers = [4,3,2,1]
# copy_numbers = numbers[:]
# numbers.sort()
# print(numbers)
# print(copy_numbers)

# captains = {}
# captains['Enterprise'] = 'Picard'
# captains['Voyager'] = 'Janeway'
# captains['Defiant'] = 'Sisko'
# if 'Enterprise' not in captains:
#     captains['Enterprise'] = 'unknown'
# if 'Discovery' not in captains:
#     captains['Discovery'] = 'unknown'
# for key in captains:
#     print(f'The {key} is captained by {captains[key]}.')
# del captains['Discovery']
# print(captains)

# captains = dict(
#     [
#         ("Enterprise", "Picard"),
#         ("Voyager", "Janeway"),
#         ("Defiant", "Sisko"),
#     ]
# )
# print(captains)

# import pathlib
# file_path = pathlib.Path.home() / "my_folder" / "my_file.txt"  # Присваиваем переменной путь к файлу
# print(file_path.exists())  # Проверка существования - True
# print(file_path.is_dir())  # Проверка на котолог - False
# print(file_path.resolve())  # Вывести абсолютный путь, но не точно
# print(file_path.absolute())  # Вывести абсолютный путь
# print(file_path.parent)  # Имя первого родительского каталога. Это сокращенная запись для .parents[0]
# print(file_path.name)  # Возвращает имя файла или каталога, на который указывает путь

# from pathlib import Path
# new_dir = Path.home() / "new_directory"  # Создаём путь
# # new_dir.mkdir()  # Создаём каталог
# new_dir.mkdir(exist_ok=True)  # Создаём каталог, есть он не существует
# print(new_dir.exists())
# print(new_dir.is_dir())
# nested_dir = new_dir / "folder_a" / "folder_b"
# nested_dir.mkdir(parents=True, exist_ok=True)  # Создать каталог со всеми родительскими каталогами. Если ещё не существует
# file_path = new_dir / 'file1.txt'  # Создаём новый путь для файла по пути home/new_directory
# file_path.touch()  # Создаём сам файл по этому пути
# # Каталог + файл
# file_path = new_dir / "folder_c" / "file2.txt"  # Создаём новый путь для файла и котолога которых ещё нет
# file_path.parent.mkdir()  # Создаёт каталог для нового файла т.к. нет каталога
# file_path.touch()  # Создаём сам файл

# import pathlib
# new_dir = pathlib.Path.home() / "new_directory"
# for path in new_dir.iterdir():  # Перебрать содержимое папки в цикле
#     print(path)
# print(list(new_dir.iterdir()))  # Возращает список файлов и папок для Path new_dir
# for path in new_dir.glob("*.txt"):  # Перебрать содержимое папки в цикле, но только файлы .txt
#     print(path)
# print(list(new_dir.glob("*.txt")))  # Тоже самое толкьо списком
# paths = [  # Создаём список путей для перебора
#     new_dir / "program1.py",
#     new_dir / "program2.py",
#     new_dir / "folder_a" / "program3.py",
#     new_dir / "folder_a" / "folder_b" / "image1.jpg",
#     new_dir / "folder_a" / "folder_b" / "image2.png",
#     ]
# for path in paths:  # Создаём файлы
#     path.touch()
# # Ищем по шаблону, но только в указанно каталоге (home/new_directory)
# print(list(new_dir.glob("*.py")))  # Все файлы .py
# print(list(new_dir.glob("*1*")))  # Все файлы с "1"
# print(list(new_dir.glob("1*")))  # Все файлы которые начинаются с "1"
# print(list(new_dir.glob("program?.py")))  # Заменяет один символ в шаблоне
# print(list(new_dir.glob("?older_?")))  # Можно указывать несколько
# print(list(new_dir.glob("1.??")))  # Подставные символы можно объединять
# print(list(new_dir.glob("program[13].py")))  # В [] указывают символы по аналогии с ?, проверяется любой из указанных символов, но только 1
# # Ищем рекурсивно в подкаталогах
# print(list(new_dir.glob("**/*.txt")))  # Все .txt включая в подкаталогах
# print(list(new_dir.rglob("*.py")))  # Все файлы .py, но рекурсивно


# import pathlib
# new_dir = pathlib.Path.home() / "new_directory"
# source = new_dir / "file1.txt"
# destination = new_dir / "folder_a" / "file1.txt"
# # source.replace(destination)  # Перемещаем файл через замену
# if not destination.exists():  # Перемещаем файл, только если нет такого файла по новому пути
#     source.replace(destination)
# # Переименовываем каталог folder_c в folder_d
# # source = new_dir / "folder_c"
# # destination = new_dir / "folder_d"
# # source.replace(destination)
# # Удаление файлов
# # file_path = new_dir / "program1.py"
# # file_path.unlink()  # Удаляем
# # file_path.unlink(missing_ok=True)  # Удаляем, без ошибки, если файл не существует
# # print(file_path.exists())  # Проверяем - False
# # Удаление каталогов. Каталог нельзя удалить, если он не пуст
# # folder_d = new_dir / "folder_d"
# # for path in folder_d.iterdir():  # Перебираем файлы в папке и удаляем их
# #     path.unlink()
# # folder_d.rmdir()  # Удаляем саму папку
# # print(folder_d.exists())
# # Удаление каталогов с содежимым
# import shutil
# folder_a = new_dir / "folder_a"
# shutil.rmtree(folder_a)  # Удаляем папку со всем содержимым
# print(folder_a.exists())

# from pathlib import Path
# path = Path.home() / "hello.txt"  # Определяем пусть файла
# path.touch()  # Создаём файл
# file = path.open(mode="r", encoding="utf-8")  # открываем файл через Path
# print(file)
# file.close()  # Закрываем файл
# # тоже самое через встроенную функцию open()
# file_path = "C:/Users/sekozlov/hello.txt"  # Определяем пусть файла
# file = open(file_path, mode="r", encoding="utf-8")  # открываем файл
# print(file)
# file.close()
# # Открытие файла с его автоматическим закрытием
# path = Path.home() / "hello.txt"  # Определяем пусть файла
# path.touch()  # Создаём файл
# with path.open(mode="r", encoding="utf-8") as file:  # объект присваивается переменной file
#     # Работа с файлом

# # Читаем файл
# from pathlib import Path
# path = Path.home() / "hello.txt"
# with path.open(mode="r", encoding="utf-8") as file:  # объект присваивается переменной file
#     text = file.read()  # файл читается и результат присваивается переменной text
# print(text)  # Выводим на экран
# # Читаем по строкам
# with path.open(mode="r", encoding="utf-8") as file:
#     for line in file.readlines():  # .readlines() возвращает итерируемый набор текстовых строк файла.
#         print(line, end="")  # end убирает пустую строку между строк


# # Записываем в файл
# from pathlib import Path
# path = Path.home() / "hello.txt"
# with path.open(mode="w", encoding="utf-8") as file:  # Открываем с w
#     file.write("Hi there!")  # Пишем строку, перезаписывая содержимое

# # Записываем в конец файла
# from pathlib import Path
# path = Path.home() / "hello.txt"
# with path.open(mode="a", encoding="utf-8") as file:
#     file.write("\nHello")

# # Записываем несколько строк
# from pathlib import Path
# lines_of_text = [
# "\nHello from Line 1\n",
# "Hello from Line 2\n",
# "Hello from Line 3 \n",
# ]
# path = Path.home() / "hello.txt"
# with path.open(mode="a", encoding="utf-8") as file:
#     file.writelines(lines_of_text)  # Пишем список

# # Работа с CSV
# from pathlib import Path
# temperature_readings = [68, 65, 68, 70, 74, 72]  # Создаём список
# file_path = Path.home() / "temperatures.csv"  # Создаём путь в файлу
# with file_path.open(mode="a", encoding="utf-8") as file:  # открываем файл в режиме присоединения
#     file.write(str(temperature_readings[0]))   # Пишем первое значение в файл
#     for temp in temperature_readings[1:]:  # Пишем остальные значения в той же строке в цикле с разделяющей запятой
#         file.write(f",{temp}")
# with file_path.open(mode="r", encoding="utf-8") as file:
#     text = file.read()  # Читаем файл
# print(text)
# temperatures = text.split(",")  # Создаём список из текста обратно
# print(temperatures)
# int_temperatures = [int(temp) for temp in temperatures]  # Приобразовываем в int
# print(int_temperatures)

# # Модуль CSV
# # csv.writer
# from pathlib import Path
# import csv
# daily_temperatures = [  # Список списков
#     [68, 65, 68, 70, 74, 72],
#     [67, 67, 70, 72, 72, 70],
#     [68, 70, 74, 76, 74, 73],
#     ]
# file_path = Path.home() / "temperatures.csv"  # Определяем путь к файлу
# """Вместо того чтобы использовать команду with, мы создаем
# файловый объект и присваиваем его переменной file, чтобы вы
# могли проанализировать каждый шаг в процессе записи данных."""
# # file = file_path.open(mode="w", encoding="utf-8", newline="")  # newline необходим для корректного перехода строк
# # writer = csv.writer(file)  # Передаём файловый обект методу csv
# # for temp_list in daily_temperatures:  # Передаём в цикле каждый список из списка
# #     writer.writerow(temp_list)  # Записываем каждый список в новую строку в файле
# # file.close()  # Закрываем файл
# # Более правильный вариант
# # with file_path.open(mode="w", encoding="utf-8", newline="") as file:  # newline необходим для корректного перехода строк
# #     writer = csv.writer(file)  # Передаём файловый обект методу csv
# # for temp_list in daily_temperatures:  # Передаём в цикле каждый список из списка
# #     writer.writerow(temp_list)  # Записываем каждый список в новую строку в файле
# # Ещё короче, записываем сразу несколько строк через .writerows
# with file_path.open(mode="w", encoding="utf-8", newline="") as file:  # newline необходим для корректного перехода строк
#     writer = csv.writer(file)  # Передаём файловый обект методу csv
#     writer.writerows(daily_temperatures)  # Записываем все списки разом в новую строку в файле

# # csv.reader
# from pathlib import Path
# import csv
# file_path = Path.home() / "temperatures.csv"  # Определяем путь к файлу
# # file = file_path.open(mode="r", encoding="utf-8", newline="")  # Открываем файл в режиме чтения
# # reader = csv.reader(file)  # csv.reader() возвращает объект чтения CSV, который может использоваться для перебора строк в файле CSV
# # for row in reader:  # Читаем каждую строку
# #     print(row)
# # file.close()
# '''Каждая строка файла CSV возвращается в виде списка строк.
# Чтобы восстановить список списков daily_temperatures,
# необходимо преобразовать каждый список строк в список целых
# чисел при помощи генератора списка'''
# daily_temperatures = []  # Создание пустого списка
# with file_path.open(mode="r", encoding="utf-8", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         int_row = [int(value) for value in row]  # Преобразование строки в список целых чисел
#         daily_temperatures.append(int_row)  # Присоединение списка целых чисел к списку daily_temperatures
# print(daily_temperatures)

# # Чтение и запись файлов CSV с заголовками
# from pathlib import Path
# import csv
# file_path = Path.home() / "employees.csv"  # Определяем путь к файлу
# file = file_path.open(mode='r', encoding='utf-8', newline='')
# reader = csv.DictReader(file)  # записывает словари с совместно используемыми ключами в строки файла CSV
# '''При создании объекта DictReader предполагается, что
# первая строка файла CSV содержит имена полей. Эти значения
# сохраняются в списке и присваиваются атрибуту .fieldnames
# экземпляра DictReader'''
# print(reader.fieldnames)
# for row in reader:  # Можно перебирать
#     print(row)
# file.close()
# def process_row(row):  # Можно преобразовать данные
#     row["salary"] = float(row["salary"])
#     return row
# with file_path.open(mode="r", encoding="utf-8", newline="") as file:
#     reader = csv.DictReader(file)  # записывает словари с совместно используемыми ключами в строки файла CSV
#     for row in reader:
#         print(process_row(row))

# # Записываем словари с ключами в CSV
# from pathlib import Path
# import csv
# people = [
#     {"name": "Veronica", "age": 29},
#     {"name": "Audrey", "age": 32},
#     {"name": "Sam", "age": 24},
#     ]
# file_path = Path.home() / "people.csv"
# file = file_path.open(mode="w", encoding="utf-8", newline="")
# writer = csv.DictWriter(file, fieldnames=["name", "age"])
# '''Когда вы создаете экземпляр DictWriter, в первом
# параметре передается файловый объект для записи данных CSV.
# Параметр fieldnames, который является обязательным,
# содержит список строк с именами полей.'''

# # SQLite
# from pathlib import Path
# import sqlite3
# connection = sqlite3.connect(Path.home() / "test_database.db")  # Ищем БД или создаём
# print(type(connection))
# cursor = connection.cursor()  # cursor объект для хранения данных
# print(type(cursor))
# query = "SELECT datetime('now', 'localtime');"  # команда SQL
# results = cursor.execute(query)  # команду передаём  в cursor.execute
# '''Команда применяет запрос к базе данных и
# возвращает объект Cursor, который присваивается переменной
# results.'''
# print(results)
# '''Чтобы получить результаты запроса, используйте
# метод results.fetchone(), который возвращает кортеж с
# первой строкой результатов'''
# row = results.fetchone()
# print(row)
# '''.fetchone() возвращает кортеж, необходимо
# обратиться к первому элементу для получения строки с
# информацией о дате и времени'''
# time = row[0]
# print(time)
# connection.close()  # Закрываем соединение

# # Использование with для управления подключением к базе данных
# from pathlib import Path
# import sqlite3
# connection = sqlite3.connect(Path.home() / "test_database.db")  # Ищем БД или создаём
# with sqlite3.connect("test_database.db") as connection:
#     cursor = connection.cursor()  # Создаём новый объект
#     query = "SELECT datetime('now', 'localtime');"  # Команда
#     results = cursor.execute(query)  # Выполняем команду
#     row = results.fetchone()  # Получаем кортеж с результатом
#     time = row[0]  # Получаем строку из кортежа
# print(time)

# # Работа с таблицами базы данных
# from pathlib import Path
# import sqlite3
# # Сначала создаются две строки с командами SQL, которые создают таблицу People и вставляют в нее данные.
# create_table = """
# CREATE TABLE People(
#     FirstName TEXT,
#     LastName TEXT,
#     Age INT
# );"""
# insert_values = """
# INSERT INTO People VALUES(
#     'Ron',
#     'Obvious',
#     42
# );"""
# connection = sqlite3.connect(Path.home() / "test_database.db")
# cursor = connection.cursor()  # cursor объект для хранения данных
# cursor.execute(create_table)  # Выполняем команды выше
# cursor.execute(insert_values)
# connection.commit()  # Сохраняем информацию в БД
# query = "SELECT * FROM People;"  # Создаём запрос
# results = cursor.execute(query)  # Выполняем запрос
# print(results.fetchone())  # Выводим запрос
# cursor.execute("DROP TABLE People;")  # Запрос на удаление таблицы (не файла)
# connection.commit()  # Сохраняем информацию в БД
# connection.close()  # Закрываем соединение

# # Тоже самое через with
# from pathlib import Path
# import sqlite3
# create_table = """
# CREATE TABLE People(
#     FirstName TEXT,
#     LastName TEXT,
#     Age INT
# );"""
# insert_values = """
#     INSERT INTO People VALUES(
#     'Ron',
#     'Obvious',
#     42
# );"""
# with sqlite3.connect(Path.home() / "test_database.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute(create_table)
#     cursor.execute(insert_values)
#     query = "SELECT * FROM People;"  # Создаём запрос
#     results = cursor.execute(query)  # Выполняем запрос
#     cursor.execute("DROP TABLE People;")  # Запрос на удаление таблицы (не файла)

# # Выполнение нескольких команд SQL
# from pathlib import Path
# import sqlite3
# sql = """
# DROP TABLE IF EXISTS People;
# CREATE TABLE People(
#     FirstName TEXT,
#     LastName TEXT,
#     Age INT
# );
#     INSERT INTO People VALUES(
#     'Ron',
#     'Obvious',
#     42
# );"""
# with sqlite3.connect(Path.home() / "test_database.db") as connection:
#     cursor = connection.cursor()
#     cursor.executescript(sql)
# '''возможно выполнить несколько сходных команд,
# вызвав метод .executemany() и передав кортеж кортежей, в
# котором каждый внутренний кортеж предоставляет информацию
# для одной команды.'''
# people_values = (
#     ("Ron", "Obvious", 42),
#     ("Luigi", "Vercotti", 43),
#     ("Arthur", "Belling", 28)
# )
# cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
# # Ещё пример
# from pathlib import Path
# import sqlite3
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# data = (first_name, last_name, age)
# with sqlite3.connect(Path.home() / "test_database.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO People VALUES(?, ?, ?);", data)
#     # cursor.execute("UPDATE People SET Age=? WHERE FirstName=?AND LastName=?;",(45, 'Luigi', 'Vercotti'))  # SQL UPDATE

# # Чтение данных SQL
# from pathlib import Path
# import sqlite3
# values = (
#     ("Ron", "Obvious", 42),
#     ("Luigi", "Vercotti", 43),
#     ("Arthur", "Belling", 28),
# )
# with sqlite3.connect(Path.home() / "test_database.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("DROP TABLE IF EXISTS People")
#     cursor.execute("""
#         CREATE TABLE People(
#             FirstName TEXT,
#             LastName TEXT,
#             Age INT
#         );"""
#     )
#     cursor.executemany("INSERT INTO People VALUES(?, ?, ?);", values)
#     # Выбрать все имена и фамилии людей, возраст которых
#     # превышает 30 лет
#     cursor.execute( "SELECT FirstName, LastName FROM People WHERE Age > 30;")
#     for row in cursor.fetchall():
#         print(row)
#     '''.fetchall() возвращает результаты запроса в
#     виде списка кортежей, в котором каждый кортеж содержит одну
#     строку данных из результатов запроса.'''

# # HTML
# from urllib.request import urlopen
# url = "http://olympus.realpython.org/profiles/aphrodite"
# page = urlopen(url)  # Открываем страницу
# # print(page)
# html = page.read().decode("utf-8") # Извлекаем HTML код и декодируем в utf-8
# # print(html)
# start_index = html.find("<title>") + len("<title>")  # Находим заголок и индекс самого заголовка
# end_index = html.find("</title>")  # Находим индекс закрывающего тега
# title = html[start_index:end_index]  # Извлекаем текст с помощаю среза
# print(title)
# # url = "http://olympus.realpython.org/profiles/poseidon"
# # page = urlopen(url)
# # html = page.read().decode("utf-8")
# # start_index = html.find("<title>") + len("<title>")
# # end_index = html.find("</title>")
# # title = html[start_index:end_index]
# # print(title)

# # Знакомство с регулярными выражениями
# import re
# from urllib.request import urlopen
# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# pattern = "<title.*?>.*?</title.*?>"
# match_results = re.search(pattern, html, re.IGNORECASE)
# title = match_results.group()
# title = re.sub("<.*?>", "", title) # Удалить теги HTML
# print(title)

# Извлечения веб-данных
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
# "html.parser" — это встроенный парсер HTML языка Python
soup = BeautifulSoup(html, "html.parser")
