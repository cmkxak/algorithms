for test_case in range(10):
    password_len = int(input())
    password = list(map(int, input().split()))
    orderCnt = int(input())
    orderList = list(input().split())
    for i in range(len(orderList)):
        if orderList[i] == 'I':
            idx = int(orderList[i+1])
            addedCnt = int(orderList[i+2])
            for j in range(addedCnt):
                password.insert(idx + j, int(orderList[i + 2 + j + 1]))
        else:
            continue
    print('#{} {}'.format(test_case+1, ' '.join(map(str, password[:10]))))