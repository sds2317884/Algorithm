def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            sum += absolutes[i] * -1
        else:
            sum += absolutes[i]
    return sum