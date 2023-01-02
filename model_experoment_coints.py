import random

def coin_flip():
    '''Считаем сколько в среднем нужно попыток бросков,
     чтобы выпадали и Орёл и Решко'''
    heads = 0
    tails = 0
    attempts = 0
    while heads == 0 or tails == 0:
        if random.randint(0, 1) == 0:
            heads += 1
            attempts += 1
        else:
            tails += 1
            attempts += 1
    return attempts

mean = 0
for i in range(10000):
    mean += coin_flip()
mean = mean / 10000
print(f'Среднее значение подбрасывания монеты из 10000 бросков: {mean:.2f}')
