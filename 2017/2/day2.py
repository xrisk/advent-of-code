check = 0
for i in range(16):
    nums = [int(x) for x in input().split()]
    check += max(nums) - min(nums)
print(check)
