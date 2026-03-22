arr = [2, 3, 4, 10, 40]
x = 10

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        print("Element found at index:", mid)
        found = True
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
