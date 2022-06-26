def solution(brown, yellow):
    answer = []
    if brown > yellow:
        answer.append((brown+yellow)//3)
    elif brown == yellow:
        answer.append(brown // 3)
        
    answer.append((brown+yellow)//answer[0])
    return answer