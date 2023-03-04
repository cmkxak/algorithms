#ATM 인출 시간 계산하기
import sys
input=sys.stdin.readline
# n=int(input())
# times=list(map(int, input().split()))
# times.sort()
# min_time=0
# for i in range(n-1):
#     times[i+1]+=times[i]
# for i in times:
#     min_time+=i
# print(min_time)

n=int(input())
p=list(map(int,input().split()))
total=0
#삽입 정렬 ver
for i in range(1, len(p)):
    while i > 0 and p[i-1] > p[i]:
        p[i-1],p[i] = p[i], p[i-1]
        i-=1
print(p)
for i in range(len(p)-1):
    p[i+1]+=p[i]
print(sum(p))



# '''
# i = 0 : t1 = t1 + t0
# i = 1 : t2 = t2 + t1
# i = 2 : t3 = t3 + t2
# i = 3 : t4 = t4 + t3
# '''