'''Випадковим чином призначте значення числовим змінним a1, a2,..., a10, a11,
a12 . Відображення значень цих змінних у таблиці нижче:
a1 a2 a3 a4
a5 a6
a7
a8 a9
'''

from random import randint

numbers = []

for _ in range(12):
    numbers.append(randint(1, 100))

print(numbers)
print()
print(numbers[0], numbers[1], numbers[2], numbers[3])
print(numbers[4], numbers[5])
print(numbers[6])
print(numbers[7], numbers[8])
