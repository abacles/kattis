votes = {}
m = 0

while True:
    s = input()
    if s == '***': break;
    votes[s] = votes.get(s, 0) + 1
    if votes[s] > m:
        m = votes[s]
        winner = s
    elif votes[s] == m:
        winner = 'Runoff!'

print(winner)
