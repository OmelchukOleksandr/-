import math
i = 1
p = 0
a = int(input('Введіть, до якого значення має відбуватись додавання: '))
while p < a:
    p += 1/math.sqrt(i)
    i+=1
    print(round(p, 2))    
