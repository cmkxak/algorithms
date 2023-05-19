t= int(input())

for test_case in range(1, t+1):
    stuCnt, hwStuCnt = map(int, input().split())
    stuInfo = {}

    for i in range(1, stuCnt + 1):
        stuInfo[i] = 1

    hwStuNum = list(map(int, input().split()))

    for i in hwStuNum:
        stuInfo[i] = 0 #과제 했으면 0으로 바뀜
    
    answer = []
    for key, val in stuInfo.items():
        if val == 1:
            answer.append(str(key))
    print("#{} {}".format(test_case, str(' '.join(answer))))