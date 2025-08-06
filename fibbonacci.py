n = 10
a = 0
b = 1
print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp