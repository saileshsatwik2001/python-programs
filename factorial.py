def factorial(n):
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

num = 5
print(f"Factorial of {num} is", factorial(num))
