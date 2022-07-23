days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = int(input('Вкажіть номер дня (від 1 до 7): '))
while 7 < day < 1:
    day = int(input('Неправильно. Спробуйте ще раз: '))
print(days[day-1])
if day < 6:
    print('Це робочий день')
else:
    print('Це вихідний день')
