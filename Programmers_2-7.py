def solution(priorities, location):
    priorities = [(v,idx) for idx,v in enumerate(priorities)]
    cnt = 0
    
    while priorities:
        if priorities[0][0] == max(priorities)[0]:
            cnt += 1
            if priorities[0][1] == location:
                break
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
    
    return (cnt)