num = 153
temp = num
order = 0
n = num
while n > 0:
    order += 1
    n //= 10

sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** order
    temp //= 10

if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")