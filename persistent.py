while True:
    line = int(input())
    if line != -1:
        digits = ""
        if line < 10:
            print('1' + str(line))
        else:
            while(line % 9 == 0):
                line //= 9
                digits += '9'
            while(line % 8 == 0):
                line //= 8
                digits += '8'
            while(line % 7 == 0):
                line //= 7
                digits += '7'
            while(line % 6 == 0):
                line //= 6
                digits += '6'
            while(line % 5 == 0):
                line //= 5
                digits += '5'
            while(line % 4 == 0):
                line //= 4
                digits += '4'
            while(line % 3 == 0):
                line //= 3
                digits += '3'
            while(line % 2 == 0):
                line //= 2
                digits+= '2'
            if len(str(line)) > 1:
                print("There is no such number.")
            else:
                print(digits[::-1])
    else:
        break
