import random

# Количество моделируемых выборов
num_elections = 10000

# Шансы кандидата A на победу на каждом участке
chances_A = [87, 65, 17]

# Счетчик побед кандидата A
wins_A = 0

for i in range(num_elections):
  # Моделируем выборы на трех участках
  votes_A = 0
  for j in range(3):
    if random.random() < chances_A[j] / 100:
      votes_A += 1
  # Учитываем победу кандидата A, если он выиграл на двух из трех участков
  if votes_A >= 2:
    wins_A += 1

# Вычисляем процент побед кандидата A
percentage_A = wins_A / num_elections * 100

print(f'Кандидат A выиграл {percentage_A:.2f}% выборов')