# Проблема 2 - http://projecteuler.net/problem=2

sum, prev, cur = 0, 0, 1

while cur < 4000000:
    prev, cur = cur, prev + cur
    if cur % 2 == 0:
        sum += cur

print(sum)