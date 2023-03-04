import sys
input=sys.stdin.readline
n=int(input())# 연산의 개수
nums=[0]*(n)
ans=[]
tmp=[]
mini=1e9
cnt=0
for i in range(len(nums)):
    x=int(input())
    if x!=0:
        ans.append(x)
    elif x==0:
        #ans에서 절댓값이 가장 작은 값 출력
        #절대값이 가장 작은 값이 여러개일 경우 이 중 가장 작은 수를 구해주어야 함.
        for i in ans: # 1 -1
            if abs(i)==mini:
                tmp.append(i)
            if abs(i)<mini:
                mini=i

        if len(ans)==0:
            print(0)

        if tmp:
            print(min(tmp))
            ans.remove(min(tmp))
        else:
            print(mini)
            ans.remove(mini)