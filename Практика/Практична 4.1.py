'''4.	Створення програми для обчислення значення функції'''
import math

x = int(input('Введіть значення x (від 5 до 24): '))

while 24 < x < 5:
    x = int(input('Введіть значення x (від 5 до 24): '))
    
if 5 <= x < 10:
    y = 1 - math.sin(x)
    
elif 10 <= x < 15:
    y = 1/2 *(1 + math.cos(x))
    
elif 15 <= x < 20:
    y = 1/3 * math.tan(x)
    
elif 20 <= x < 25:
    y = 1/(math.tan(x))**3

print('Значення y: ', '%.2f' %y)

        
