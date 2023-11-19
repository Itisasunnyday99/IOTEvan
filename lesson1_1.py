import random as rd

m = 0
for i in range(100):
    n = rd.randint(1, 50)
    print(n, end=' ')
    if n == 25:
        m += 1

print('\n 25出現了', m, '次')
