import heapq, sys

n = 0
for line in sys.stdin:
    line = line.strip()
    if n == 0:
        n = int(line)
        s = []
        q = []
        h = []
        q_read = 0
        s_possible = q_possible = h_possible = True
    else:
        m, x = [int(_) for _ in line.split()]
        if m == 1:
            s.append(x)
            q.append(x)
            heapq.heappush(h, -x)
        else:
            if len(s) == 0:
                s_possible = q_possible = h_possible = False
            else:
                if s.pop() != x:
                    s_possible = False
                if q[q_read] != x:
                    q_possible = False
                q_read += 1
                if heapq.heappop(h) != -x:
                    h_possible = False
        n -= 1
        if n == 0:
            if s_possible or q_possible or h_possible:
                if int(s_possible) + int(q_possible) + int(h_possible) > 1:
                    print('not sure')
                elif s_possible:
                    print('stack')
                elif q_possible:
                    print('queue')
                else:
                    print('priority queue')
            else:
                print('impossible')
