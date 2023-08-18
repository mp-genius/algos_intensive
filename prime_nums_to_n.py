n = int(input())

nums = [i for i in range(1, n + 1)]

i = 1
while i < len(nums):
    j = i+1
    while j < len(nums):
        if nums[j] % nums[i] == 0:
            nums.pop(j)
        j+=1
    i += 1

print(nums)
