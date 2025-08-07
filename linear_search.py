arr = [5, 3, 7, 1, 9]
target = 7
found = False
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element found at index {i}")
        found = True
        break
if not found:
    print("Element not found")