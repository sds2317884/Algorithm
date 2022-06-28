def solution(num):
    i = num
    n = 0
    while i > 1:
        n+=1
        if n >= 500:
            return -1
        if i == 1:
            return 0
        if i % 2 == 0:
            i = i // 2
        elif i % 2 == 1:
            i = (i * 3) + 1
        
        
        
        
    return n