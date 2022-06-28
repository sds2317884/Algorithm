from math import gcd

def solution(arr):
    answer = arr[0]
    
    for n in arr:
        answer = answer*n // gcd(answer,n)
    
    return answer