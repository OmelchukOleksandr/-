def mediana(d, e, f):
    global ma, mb, mc
    ma = 0,5*(2*e**2 + 2*f**2 - d**2)**0.5
    mb = 0,5*(2*d**2 + 2*f**2 - e**2)**0.5
    mc = 0,5*(2*e**2 + 2*d**2 - f**2)**0.5
    print(ma, mb, mc)

a = float(input('Значення a: '))
b = float(input('Значення b: '))
c = float(input('Значення c: '))

if a<=b+c and b<=a+c and c<=a+b:
    mediana(a, b, c)
    print (ma, mb, mc)
    mediana(ma[1], mb[1], mc[1])
    print (ma, mb, mc)
else:
    print('Такого трикутника не існує.')
