# Problem 10: Find all factors of a number
num = 36
print("Factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")