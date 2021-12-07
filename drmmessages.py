def rotate(s):
    r = sum([ord(ch)-ord('A') for ch in s])
    final = ''
    for ch in s:
        final += chr(ord('A') + (ord(ch)-ord('A')+r)%26)
    return final

drm = input()
a, b = drm[:len(drm)//2], drm[len(drm)//2:]

a, b = rotate(a), rotate(b)
orig = ''
for i in range(len(a)):
    orig += chr(ord('A') + (ord(a[i]) + ord(b[i]) - 2 * ord('A')) % 26)

print(orig)
