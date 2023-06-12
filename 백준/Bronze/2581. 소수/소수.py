import math

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


m = int(input())
n = int(input())
ans = []

for i in range(m, n+1):
    if isPrime(i):
        ans.append(i)

if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)