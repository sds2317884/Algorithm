def solution(phone_book) :
    answer = True
    dic = {}
    
    for p in phone_book:
        dic[p] = 1
        
    for p in phone_book:
        tmp = ''
        for num in p :
            tmp += num
            if tmp in dic and tmp != p:
                answer = False
    return answer