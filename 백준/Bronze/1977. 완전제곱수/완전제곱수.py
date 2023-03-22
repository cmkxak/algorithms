#완전제곱수
n=int(input())
m=int(input())
res=[]
for i in range(n,m+1):
    tmp= i ** 0.5
    if int(i ** 0.5) == tmp:
        res.append(i)
if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)