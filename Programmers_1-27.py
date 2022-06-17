def solution(n):
    answer = list(str(int(n)))
    answer.sort(reverse=True)
    answer = int(''.join(answer))
    return answer