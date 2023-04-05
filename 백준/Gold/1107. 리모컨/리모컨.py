import sys
input = sys.stdin.readline
#리모컨
remote=[0,1,2,3,4,5,6,7,8,9]
n = int(input())
k = int(input()) #고장난 리모컨 갯수
dis_remote = list(map(int, input().split())) #고장난 리모컨 리스트
ans = abs(100 - n)
remote = [str(i) for i in remote if i not in dis_remote] #아래에서 가능한 리모컨만 누르도록 비교해주기 위해 str 타입으로 대입

#0-1000000까지 단순히 탐색한다.
#단, 가능한 리모컨 숫자만 눌러야 한다.
for i in range(1000001):
    for j in str(i):
        if j not in remote:
            break
    else:
        #(숫자버튼을 누른 횟수) + (+/-버튼을 누른 횟수)
        ans = min(ans, len(str(i)) + abs(i - n))
print(ans)