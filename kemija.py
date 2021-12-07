vowels = {'a', 'e', 'i', 'o', 'u'}
code = input()
msg = []

i = 0
while i < len(code):
    msg.append(code[i])
    if code[i] in vowels:
        i += 2 # skip next two characters
    i += 1

print(''.join(msg))
