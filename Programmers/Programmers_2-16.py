from itertools import permutations

def solution(numbers):
    answer = []
    per = []
    numbers = list(numbers)
    
    for i in range(1,len(numbers)+1):
        answer += list(permutations(numbers,i))
    a = [int(''.join(p)) for p in answer]
    
    for n in a:
        if n < 2:
            continue
        check = True
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                check = False
                break
        if check:
            per.append(n)
        
    return len(set(per))
    