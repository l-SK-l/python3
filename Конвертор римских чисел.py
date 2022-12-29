# romans_number =	dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
romans_number =	{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_arabic(roman_string):
  # Инициализируем счетчик результата
  result = 0
  # Перебираем символы строки в обратном порядке
  for i in range(len(roman_string)-1, -1, -1):
    # Получаем текущий символ римского числа
    curr_symbol = roman_string[i]
    # Получаем значение текущего символа из словаря
    curr_value = romans_number[curr_symbol]
    # Если текущее значение меньше или равно предыдущего, то просто добавляем его к результату
    if curr_value <= result:
        # if i <= len(roman_string) - 2:
        #     result += curr_value
        # else:
        #     result -= curr_value
        result -= curr_value
    # В противном случае вычитаем его из результата
    else:
      result += curr_value
    print(result)
 
#   result = abs(result)
  # Возвращаем результат
  print(result)
#   return result

# converter_from_roman_number(input('Введите римское число: '))
roman_to_arabic(input('Введите римское число: '))
