arr = [12, 35, 1, 10, 34, 1]

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

if second == float('-inf'):
    print("No second largest element.")
else:
    print("Second largest element is:", second)