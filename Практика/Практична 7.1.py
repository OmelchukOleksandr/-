a0 = 0
a1 = 1
a2 = 2
a3 = 3
def p(y):
    p = a3 * y**3 + a2 * y**2 + a1 * y + a0
    return p 

#p = lambda y: a3 * y**3 + a2 * y**2 + a1 * y + a0
for x in range(4):
    print('x =', x, '. p(', x, '+ 1) - p(', x, ')= ', p(x+1)-p(x))
'''def p():
    for x in range(4):
        print('x =', x, '. p(', x, '+ 1) - p(', x, ')= ', (a3 * (x+1)**3 + a2 * (x+1)**2 + a1 * (x+1) + a0)-(a3 * x**3 + a2 * x**2 + a1 * x + a0))
p()'''
    

