# #  main.py
# # import mypackage.module1
# # import mypackage.module2
# from mypackage import module1, module2
# # from mypackage.module1 import greet
# # from mypackage.module2 import depart

# # mypackage.module1.greet("Pythonista")
# # mypackage.module2.depart("Pythonista")
# module1.greet("Pythonista")
# module2.depart("Pythonista")

from mypackage.module1 import greet
from mypackage.mysubpackage.module3 import people

for person in people:
    greet(person)