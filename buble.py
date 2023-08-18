arr = list(map(int, input().split()))

def buble_sort(array):
    num_changes = 0
    for i in range(1, len(arr)):
        if array[i] < array[i-1]:
            array[i-1], array[i] = array[i], array[i-1]
            num_changes += 1
    return num_changes, array

num_changes, array = buble_sort(arr)

while num_changes != 0:
    num_changes, array = buble_sort(array)

print(array)