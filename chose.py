arr = list(map(int, input().split()))

for i in range(len(arr)):
    min_val_ind = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_val_ind]:
            min_val_ind = j
    arr[i], arr[min_val_ind] = arr[min_val_ind], arr[i]

print(arr)