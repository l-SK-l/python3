# Играют два игрока.  
# Есть 10 палочек. 
# Игроки по очереди берут от одной до трёх палочек. 
# Играют до тех пор пока не закончатся палочки.
# Тот кто взял последним - тот проиграл.
# Реализуйте игру таким образом, чтобы могли играть два человека. Изначально есть 10 палочек. 
# На каждом ходу выводите на консоль текущее количество оставшихся палочек и просите ввести количество палочек, которое хочет взять игрок (который делает ход). 
# Не забывайте менять очерёдность игроков и сокращать кол-во палочек. В конце надо вывести кто победил - первый или второй игрок.
 
# Приветствие
print('''                   Привет user_name!
        Сейчас вы со своим другом сыграете в игру Палочки!
Правила: 
      Есть N палочек, 2 игрока берут палочки по очереди!
          За один раз можно взять от 1 до 3 палочек
        Игра идёт до тех пор, пока не закончатся палочки
         Тот кто взял последним - тот проиграл.''')

all_sticks = 10
take_sticks = 0
i = 0
player_one_sticks = 0
player_two_sticks = 0
player_one_name = 'Один'
player_two_name = 'Два'

def showing_sticks():  # показываем текущее число палочек
    return print(f'Осталось {all_sticks} палочек!')

def showing_winner(name):  # Показываем победиетля, если игрок оставил одну палочку
    print(f'Кажется игрок у нас есть победитель! Игрок {name} победил!')

def showing_another_winner(name):  # Показываем победите, если игрок взял последнюю палочку
    print(f'О нет, палочки закончились! Игрок {name} победил!')

def taking_sticks(name):  # Проверяем сколько палочек взял игрок
    while True:
        user_input = input(f'Сколько игрок {name} хочет взять палочек: ')
        if not user_input.isdigit():  # Если user_input не является целым числом
            print('Это не целое число! Попробуйте еще раз.')
            continue  # Возвращаемся в начало цикла
        take_sticks = int(user_input)  # Преобразуем user_input в целое число
        if take_sticks < 1 or take_sticks > 3:  # Если take_sticks не в диапазоне от 1 до 3
            print('Число не в диапазоне от 1 до 3! Попробуйте еще раз.')
            continue  # Возвращаемся в начало цикла
        return take_sticks  # Если все условия выполнены, возвращаем take_sticks

# Для начала нажми любую клавишу
input('Нажмите любую клавишу для продолжения...')

# Спрашиваем столько будет палочек
# Проверяем, что введено положительное число от 10 до 50
while i < 1:
    try:
        all_sticks = input('Сколько будет палочек? (10): ')
        if all_sticks == '':  # Если игрок ничего не вводит, то используется значение по умолчанию
            all_sticks = 10
            break
        all_sticks = int(all_sticks)
    except ValueError:  # Если игрок вводит не целое число, то будет ошибка ValueError и возрат в начало цикла
        print('Нужно ввести целое число от 10 до 50. Попробуй ещё раз!')
        continue
    if all_sticks < 10 or all_sticks > 50:  # Проверка целого числа
        print('Нужно ввести целое число от 10 до 50. Попробуй ещё раз!')
    else:
        i += 1
showing_sticks()

# Сама игра
while True:  # Просим ввести число в цикле двух игроков
    if player_one_sticks < all_sticks - 1:  
        all_sticks -= taking_sticks(player_one_name)  # Просим взять 1-3 палочки и отнимаем их из общего числа
        showing_sticks()
        if all_sticks == 0:  # Проверяем, что игрок не взял последние палочки, показываем противоположного игрока
            showing_another_winner(player_two_name)
            break
        elif all_sticks <= 1:  # Проверяем, что игрок оставил одну палочку, воводим имя победителя
            showing_winner(player_one_name)
            break
    if player_two_sticks < all_sticks - 1:
        all_sticks -= taking_sticks(player_two_name)  # Просим взять 1-3 палочки и отнимаем их из общего числа
        showing_sticks()
        if all_sticks == 0:  # Проверяем, что игрок не взял последние палочки, показываем противоположного игрока
            showing_another_winner(player_one_name)
            break
        elif all_sticks <= 1:  # Проверяем, что игрок оставил одну палочку, воводим имя победителя
            showing_winner(player_two_name)
            break
