def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)

    for i in reserve:

        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    answers = n - len(lost)
    return answers

a = [3]
b = [1]
print(solution(3,a,b))