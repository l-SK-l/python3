import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

state, capital = random.choice(list(capitals_dict.items()))

exit = 'exit'

while True:
    answer = input(f'Напишите название сталицы штата {state}: ').lower()
    if answer == exit.lower():
        print(f'Goodbay')
        break
    elif answer != capital.lower():
        print(f'Неверно! Поробуйте ещё раз!')
        continue
    else:
        print(f'Correct')
        break

# OR
# while True:
#     guess = input(f"What is the capital of '{state}'? ").lower()
#     if guess == "exit":
#         print(f"The capital of '{state}' is '{capital}'.")
#         print("Goodbye")
#         break
#     elif guess == capital.lower():
#         print("Correct! Nice job.")
#         break
