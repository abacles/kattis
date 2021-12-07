cases = int(input())
for i in range(cases):
    num = int(input())
    if num%2 == 0:
        print(str(num) + ' is even')
    else:
        print(str(num) + ' is odd')
