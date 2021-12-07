import sys

for line in sys.stdin:
    nums = [int(_) for _ in line.split()]
    bigsum = sum(nums)
    for i in range(len(nums)):
        if nums[i] == bigsum - nums[i]:
            print(nums[i])
            break
