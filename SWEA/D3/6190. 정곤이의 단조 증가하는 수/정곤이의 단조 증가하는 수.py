t=int(input())
for test_case in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    operatedNums = []
    answer = []
    for i in range(n):
        for j in range(i+1, n):
            operatedNums.append(nums[i] * nums[j])
            
    for num in operatedNums:
        if num > 10:
            num = str(num)
            for j in range(len(num) - 1):
                if num[j] > num[j + 1]:
                    break
            else:
               answer.append(int(num))
    if answer:
        print("#{} {}".format(test_case, max(answer)))
    else:
        print("#{} {}".format(test_case, -1))