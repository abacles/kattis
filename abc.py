nums = sorted([int(_) for _ in input().split()])
order = input()
print(nums[ord(order[0])-65],nums[ord(order[1])-65],nums[ord(order[2])-65])
