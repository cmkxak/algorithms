#stack 수열
import sys
input=sys.stdin.readline
n=int(input())
a=[0]*(n)

#수열을 입력받는다.
for i in range(n):
    a[i]=int(input())

cnt=1
operate_list=[]
stack=[]
result=True #NO가 출력되는 경우엔 저장된 연산 순서를 나타내지 않기 위해
for i in range(n):
    if a[i] >= cnt:
        while a[i] >= cnt:
            stack.append(cnt)
            cnt+=1
            operate_list.append('+')
        stack.pop()
        operate_list.append('-')
    elif a[i] < cnt:
        removed_val=stack.pop()
        if removed_val > a[i]: #스택에서 pop 한 결과 값 > 현재 수열의 수
            print("NO")
            result = False
            break
        else:
            operate_list.append('-')
if result:
    for i in operate_list:
        print(i)