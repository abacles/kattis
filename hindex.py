def f(papers, i):
    return papers[i] - (len(papers) - i)

n = int(input())
papers = [int(input()) for i in range(n)]

papers.sort()

lo, hi = 0, n-1
while lo < hi:
    mid = (lo + hi) // 2
    val = f(papers, mid)
    if val < 0:
        lo = mid + 1
    elif val > 0:
        hi = mid
    else:
        lo = mid
        break

print(n - lo if f(papers, lo) >= 0 else 0)
