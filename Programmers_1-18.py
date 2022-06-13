def solution(num):
    if num % 2 == 1:
        return "Odd"
    elif num % 2 == 0 or num == 0:
        return "Even"