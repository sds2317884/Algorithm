def solution(A,B):
    
    sum = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        sum += (A[i]*B[i])
    
    return sum