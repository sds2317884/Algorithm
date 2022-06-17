def solution(n, m):
    answer = []
    c, d = max(n,m), min(n,m)
    t = 1
    while t > 0:
        t = c % d
        c,d = d,t
    answer = [c, int((n*m)/c)]
    return(answer)
