a,b,top = [int(_) for _ in input().split()]
for i in range(1,top+1):
    if i % a == 0:
        print('Fizz',end='')
    if i % b == 0:
        print('Buzz',end='')
    if i % a != 0 and i % b != 0:
        print(i,end='')
    print()
