import random
a = []
b = []

for _ in range(3):
    a.append([0]*3)
    b.append([0]*3)

for i in range(3):
    for j in range(3):
        a[i][j] = random.randint(0, 10)
        b[i][j] = random.randint(0, 10)

ab = [[a[0][0]+b[0][0], a[0][1]+b[0][1], a[0][2]+b[0][2]],
      [a[1][0]+b[1][0], a[1][1]+b[1][1], a[1][2]+b[1][2]],
      [a[2][0]+b[2][0], a[2][1]+b[2][1], a[2][2]+b[2][2]]]

print(a, '\n', b, '\n', ab)

tab = [[ab[0][0], ab[1][0], ab[2][0]],
       [ab[0][1], ab[1][1], ab[2][1]],
       [ab[0][2], ab[1][2], ab[2][2]]]
print()
print(tab)
