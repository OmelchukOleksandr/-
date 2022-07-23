import random
numbers = set()
rand = set()
while len(numbers)< 10:
    numbers.add(random.randint(1, 40))
print(numbers)

while len(rand) < 5:
    for n in numbers:
        a = random.randint(1,2)
        if a == 1:
            rand.add(n)
        if len(rand) == 5:
            break
print(rand)   
