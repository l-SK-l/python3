# #  main.py
import helpers.math
import helpers.string
# from helpers import module1, module2


# # helpers.module1.greet("Pythonista")
# # helpers.module2.depart("Pythonista")
# module1.greet("Pythonista")
# module2.depart("Pythonista")

length = 5
width = 8
text = helpers.string.shout(f'the are a {length}-by-{width} rectangle is {helpers.math.area(5, 8)}')
print(text)
# OR
text = f'the are a {length}-by-{width} rectangle is {helpers.math.area(5, 8)}'
print(helpers.string.shout(text))