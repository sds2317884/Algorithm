from itertools import combinations

def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for i in range(2,(num//2)+1):
            if num%i == 0:
                return False
        return True
   
def solution(nums):
    a = 0
    cmb = list(combinations(nums,3))  
    for i in cmb:
        if is_prime_number(sum(i)):
            a+=1
    return a    