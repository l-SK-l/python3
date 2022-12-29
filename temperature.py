
def conver_cel_to_far(C):
    F = C * 9 / 5 + 32
    return F

def cenvert_far_to_cel(F):
    C = (F - 32) * 5 / 9
    return C

Far = float(input(f'Enter a temperature in degrees F: '))
print(f'{Far} degrees F = {cenvert_far_to_cel(Far):.2f} degrees C')

Cel = float(input(f'Enter a temperature in degrees C: '))
print(f'{Cel} degrees C = {conver_cel_to_far(Cel):.2f} degrees F')