nums = [int(input()) for _ in range(10)]
distinct = []
for n in nums:
    if not n % 42 in distinct:
        distinct.append(n % 42)
print(len(distinct))
