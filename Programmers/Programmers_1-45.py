def solution(numbers):
    sum = 0
    number = [0,1,2,3,4,5,6,7,8,9]
    numbers.sort()
    for i in number:
        if i not in numbers:
            sum += i
    return sum