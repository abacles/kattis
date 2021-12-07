n, c = [int(_) for _ in input().split()]
nums = [int(_) for _ in input().split()]
freq = {}
first = {}
for i in range(n):
    if nums[i] in freq:
        freq[nums[i]] += 1
    else:
        freq[nums[i]] = 1
        first[nums[i]] = i

data = [(-freq[i], first[i], i) for i in freq]
data.sort()

nums = []
for x in data:
    nums.extend([x[2]] * -x[0])
    
print(' '.join(str(_) for _ in nums))
