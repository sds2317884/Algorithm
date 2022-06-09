def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x:0 for x in id_list}

    for r in set(report) :
        reports[r.split()[1]] += 1

    for r in set(report) :
        if reports[r.split()[1]] >= k :
            answer[id_list.index(r.split()[0])] += 1



    return answer


a = ["muzi", "frodo", "apeach", "neo"]
b = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

print(solution(a,b,2))
