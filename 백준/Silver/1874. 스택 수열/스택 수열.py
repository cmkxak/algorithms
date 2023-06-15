#stack 수열
n=int(input())
a=[0]*(n)

#수열을 입력받는다.
for i in range(n):
    a[i]=int(input())

cnt=1
operate_list=[]
stack=[]
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

        if removed_val > a[i]:
            print("NO")
            exit()
        else:
            operate_list.append('-')
for i in operate_list:
    print(i)