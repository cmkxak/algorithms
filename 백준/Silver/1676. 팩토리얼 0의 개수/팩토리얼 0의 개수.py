def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *=i
    return result

n=int(input())
nums = str(factorial(n))
cnt=0
for i in range(len(nums)-1, -1, -1):
    if int(nums[i]) != 0:
        break
    else:
        cnt+=1
print(cnt)