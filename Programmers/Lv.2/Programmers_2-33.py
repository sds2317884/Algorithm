from re import L
import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a=[list(map(int,input().split())) for _ in range(n)]
largest=[]
sum3=0
sum4=0
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    sum3+=a[i][i]
    sum4+=a[i][-(1+i)]
    largest.append(sum1)
    largest.append(sum2)
largest.append(sum3)
largest.append(sum4)

print(max(largest))
