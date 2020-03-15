def cut_cake(people):
    try:
        parts = 1 / people
        print(f"Каждый человек получит {parts} пирога")
    except (ZeroDivisionError, TypeError):
        print("Не надо делить на ноль")


import random

while True:
    people = random.randint(1, 10)
    cut_cake(people)