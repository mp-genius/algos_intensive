arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    cur_elem = i
    insert = arr[cur_elem]
    while cur_elem - 1 >= 0 and arr[cur_elem - 1] > insert:
        arr[cur_elem] = arr[cur_elem - 1]
        cur_elem -= 1
    arr[cur_elem] =  insert

print(arr)

