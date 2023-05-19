t = int(input())

for test_case in range(1, t + 1):
    stuCnt, hwStuCnt = map(int, input().split())
    stuInfo = []

    for i in range(1, stuCnt + 1):
        stuInfo.append(str(i))

    hwStu = list(map(str, input().split()))

    for i in hwStu:
        idx = stuInfo.index(i)
        stuInfo.pop(idx)

    print("#{} {}".format(test_case, str(' '.join(stuInfo))))