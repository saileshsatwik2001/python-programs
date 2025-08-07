arr = [1, 3, 5, 7, 9, 11]
target = 7
low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(f"Element found at index {mid}")
        found = True
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")