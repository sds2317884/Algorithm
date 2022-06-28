def solution(prices):
    answer = []
    
    while prices:
        cnt = 0
        pri = prices.pop(0)

        for i in prices:
            cnt += 1
            if pri > i:
                break

        answer.append(cnt)
    return answer

a = [1, 2, 3, 2, 3]
print(solution(a))