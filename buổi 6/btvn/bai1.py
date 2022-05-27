arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list\t: {arr}")
for i in range(len(arr)):
    arr[i] = arr[i] + 2
print(f"Add 2\t\t: {arr}")
for i in range(len(arr)):
    arr[i] = arr[i] - 2
    arr[i] = arr[i] * 2
print(f"Multiply by 2\t: {arr}")
for i in range(len(arr)):
    arr[i] = arr[i] / 2
arr.append(arr[0])
arr.append(arr[1])
arr.pop(0)
arr.pop(1)
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(f"Shift 2\t\t: {arr}")