def is_prime(x):
    global cnt
    if x < 2:
        return
    for i in range(2, x):
        if x % i == 0:
            return
    cnt+=1
    return cnt

n = int(input())
nums = list(map(int, input().split())) # 1,3,5,7
cnt = 0
for i in nums:
    is_prime(i)
print(cnt)