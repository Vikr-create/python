arr = [10, 25, 7, 40, 15]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest:", largest)