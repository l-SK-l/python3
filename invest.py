def procent(amount, rate):
    return (amount * rate) / 100

def invest(amount, rate, years):
    for x in range(1, years + 1):
        result = amount + procent(amount, rate)
        print(f'year {x}: ${result:.2f}')
        amount = result

amount = float(input(f'Your amount: $'))
rate = float(input(f'Your rate in %: '))
years = int(input(f'How mane years: '))

result = invest(amount, rate, years)
