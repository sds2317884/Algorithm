def move(frm, to, mid, n, answer):
    if n==1:
        answer.append([frm,to])
        return
    #1.
    move(frm, mid, to, n - 1, answer)
    #2.
    answer.append([frm,to])
    #3.
    move(mid, to, frm, n - 1, answer)

def solution(n):
    answer = []
    move(1, 3, 2, n, answer)
    return answer