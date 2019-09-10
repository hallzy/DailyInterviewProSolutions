def staircase(n):
    # Fill this in.
    if n <= 0:
        return None
    return fibonacci(n+1)

def fibonacci(n):
    if n < 0:
        return None

    if n <= 1:
        return n;

    # First 2 fibonacci numbers
    num1 = 0
    num2 = 1

    for x in range(1, n):
        sumVal = num1 + num2
        num1 = num2
        num2 = sumVal
    return sumVal

print staircase(0) == None
print staircase(1) == 1
print staircase(2) == 2
print staircase(3) == 3
print staircase(4) == 5
print staircase(5) == 8
print staircase(6) == 13
