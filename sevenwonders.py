sci = input()
t,c,g = sci.count('T'),sci.count('C'),sci.count('G')
print(t**2 + c**2 + g**2 + 7 * min(t,c,g))
