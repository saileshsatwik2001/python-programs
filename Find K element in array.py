arr = [7, 10, 4, 3, 20, 15]
k = 3

n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(f"{k}th Minimum:", arr[k-1])
print(f"{k}th Maximum:", arr[-k])