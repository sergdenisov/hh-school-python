# Проблема 3 - http://projecteuler.net/problem=3

factors, d, n = [], 2, 600851475143
while n > 1:
    while n % d == 0:
        factors.append(d)
        n /= d
    d += 1

largest_prime_factor = max(factors)
print(largest_prime_factor)