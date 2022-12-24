import random 

print('''Привет! Я загадал число от 1 до 50, угадай его!
      У тебя есть всего 6 попыток! 
     Но я буду тебе подсказывать ;-) ''')
# Генерируем число от 1 до 50.
secret_number =  random.randint(1, 50)
# Объявляем переменные.
user_number = ''
i = 1
tries = 6 

# Цикл работает пока число макс попыток не равно 1, при каждой ошибки уменьшается число попыток
# Цикл предлогает ввести текст и проверяет, что он int
while i != tries:
    try:
        user_number = input('Введи целое число от 1 до 50: ')
        number = int(user_number)
    except ValueError:
        print('Это не целое число! Попробуй ещё раз!')
        continue
    if number < secret_number:
        print(f'Неверно! Моё число больше, чем {number}!')
        tries -= 1
    elif number == secret_number:
        print(f'Ты угадал! Я загадал число {secret_number}!')
        break
    else:
        print(f'Неверно! Моё число меньше, чем {number}!')
        tries -= 1
if tries == 1:
    print(f'Не угадал) Ну ты Лох!')
