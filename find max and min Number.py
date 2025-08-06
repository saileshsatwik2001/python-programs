arr = [10, 3, 5, 2, 8]
max_elem = arr[0]
min_elem = arr[0]

for num in arr[1:]:
    if num > max_elem:
        max_elem = num
    if num < min_elem:
        min_elem = num

print("Maximum:", max_elem)
print("Minimum:", min_elem)