num = 28
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")