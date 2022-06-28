def solution(array, commands):
    num = []
    for i in range(len(commands)):
        answer = []
        for j in range(commands[i][0]-1,commands[i][1]):
            answer.append(array[j])
        answer.sort()
        num.append(answer[commands[i][2]-1])
    return(num)
        