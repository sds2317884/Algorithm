import sys
sys.stdin = open("input.txt","rt")

answer = []
n = int(input())
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a,b,c=map(int, tmp)
    
    if a==b and b==c:
        answer.append(10000+(a*1000)) 
    elif a==b or a==c:
        answer.append(1000+(a*100))
    elif b==c:
        answer.append(1000+(b*100))
    else:
        answer.append(c*100)

print(int(max(answer)))

