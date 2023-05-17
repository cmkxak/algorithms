for test_case in range(10):
    pwLen = int(input())
    pw = list(map(int, input().split()))
    orderCnt = int(input())
    orderList = list(input().split())
    
    for i in range(len(orderList)):
        if orderList[i] == 'I':
            idx = int(orderList[i+1])
            addedCnt = int(orderList[i+2])
            for j in range(addedCnt):
                pw.insert(idx + j, int(orderList[i + 2 + j + 1]))

        elif orderList[i] == "D":
            idx = int(orderList[i+1])
            deletedCnt = int(orderList[i+2])
            for j in range(deletedCnt):
                pw.pop(idx + j)

        elif orderList[i] == "A":
            addedCnt = int(orderList[i+1])
            for j in range(addedCnt):
                pw.append(int(orderList[i + 2 + j]))

        else:
            continue

    print("#{} {}".format(test_case +1, ' '.join(map(str, pw[:10]))))
