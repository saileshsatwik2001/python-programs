arr = [2, 8, 1, 9, 4]
max_elem = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max_elem:
        max_elem = arr[i]

print("Largest element is:", max_elem)