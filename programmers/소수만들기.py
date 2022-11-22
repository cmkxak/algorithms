def check_sosu(nums):
    answer = 0
    for i in range(2, nums//2 +1):
        if nums % i == 0:
            answer+=1
    if answer == 0:
        return True
    else:
        return False

def solution(nums):
    s = 0
    e = len(nums) - 1
    answer = 0

    while s != e:
        for i in range(1,e):
            if check_sosu(nums[s] + i + e):
                answer+=1
    print(answer)

nums = [1,2,3,4]
solution(nums)