# Проблема 9 - http://projecteuler.net/problem=9

sum, product = 1000, 1

for a in range(1, round(sum/3) + 1):
    for b in range(a + 1, round(sum/2) + 1):
        c = sum - a - b
        if (c > 0 and (a**2 + b**2 == c**2)):
            product = a * b * c
            print('a={:d}, b={:d}, c={:d}'.format(a, b, c))
            print(product)