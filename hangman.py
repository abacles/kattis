secret = set(input())
guesses = input()
correct = incorrect = 0
for ch in guesses:
    if ch in secret:
        correct += 1
    else:
        incorrect += 1
    if correct == len(secret) or incorrect == 10:
        break
print('WIN' if correct == len(secret) else 'LOSE')
