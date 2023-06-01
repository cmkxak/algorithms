def get_divide_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x//=10
    return sum

n = int(input())
ans = []
for i in range(1, n):
    if (get_divide_sum(i) + i) == n:
        ans.append(i)
if ans:
    print(min(ans))
else:
    print(0)