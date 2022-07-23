'''Вар 11'''
import math
x = int(input('Введіть значення x '))
y = int (input('Введіть значення y '))
z = int (input('Введіть значення z '))

a = (2 + x)*(1+y/(x**2 + 3))/(y**2 + 1/(z**2 + 4))
b = (1 + math.tan(x/2)**2)**2

print('Значення a', a)
print('Значення b', b)
