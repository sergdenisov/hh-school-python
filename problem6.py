# Проблема 6 - http://projecteuler.net/problem=6

sumOfSquares, squareOfSum = 0, 0

for i in range(1, 101):
    sumOfSquares += i ** 2
    squareOfSum += i

squareOfSum *= squareOfSum
dif = squareOfSum - sumOfSquares
print(dif)