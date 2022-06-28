def solution(sizes):
    a = []
    b = []
    for i in range(len(sizes)):
        sizes[i].sort()
        a.append(sizes[i][0])
        b.append(sizes[i][1])
    return max(a)*max(b)
