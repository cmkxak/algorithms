import sys
input=sys.stdin.readline()
a,b=map(int,input.split())
n=list(map(int,input.split()))
s=[0]
sum=0
for i in n:
   sum+=i
   s.append(sum)
for i in range(b):
    x,y=map(int,input.split())
    print(s[y]-s[x-1])