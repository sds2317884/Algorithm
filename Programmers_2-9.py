def solution(prices):
    answer = []
    
    while prices:
        cnt = 0
        pri = prices.pop(0)
        if len(prices) == 0:
            answer.append(0)
            
        for i in prices:
            if prices and pri <= i:
                cnt += 1
            else:
                cnt += 1
                break
            
        if cnt:
            answer.append(cnt)
    return answer