import sys
input=sys.stdin.readline
prime_num=[]
def is_prime(x):
    global sum
    if x < 2:
        return
    for i in range(2, x):
        if x % i == 0:
            return
    sum+=x
    prime_num.append(x)
m=int(input())
n=int(input())
sum=0
for i in range(m, n+1):
    is_prime(i)
if len(prime_num) == 0:
    print(-1)
else:
    print(sum)
    print(min(prime_num))