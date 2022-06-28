def solution(s):
    answer = s.lower()
    a = answer.count("p")
    b = answer.count("y")
    print(a,b)
    
    return a==b