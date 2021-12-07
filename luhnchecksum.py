for c in range(int(input())):
    num = input()
    checksum = 0
    for i in range(len(num)-1, -1, -2):
        checksum += int(num[i])
    for i in range(len(num)-2, -1, -2):
        double = 2 * int(num[i])
        checksum += double%9 if double!=9 and double!=18 else 9
    print('PASS' if checksum % 10 == 0 else 'FAIL')
