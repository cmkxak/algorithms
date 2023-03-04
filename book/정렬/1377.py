#버블정렬 1
import sys
input=sys.stdin.readline

n=int(input())
A=[]

for i in range(n):
    A.append((int(input()), i))

print(A)
ans=0
new_A=sorted(A)
print(new_A)

for i in range(n):
    ans=max(ans, new_A[i][1] - i)
print(ans+1)