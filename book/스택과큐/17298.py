n=int(input()) #수열의 크기 입력
ans=[0] * n
A=list(map(int,input().split())) # 문제에서 주어진 수열
mystack=[]
print(ans)

for i in range(n):
    while mystack and A[mystack[-1]] < A[i]:
        ans[mystack.pop()]=A[i]
    mystack.append(i)

#반복문을 다 돌고 나왔는데 스택이 비어있지 않은 경우
while mystack:
    ans[mystack.pop()]=-1 #오큰수가 없는 경우 이므로 -1

for i in ans:
    print(i, end=' ')
