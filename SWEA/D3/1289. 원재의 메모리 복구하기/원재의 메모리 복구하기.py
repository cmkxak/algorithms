t=int(input())
for tc in range(1, t+1):
    ori = list(input())
    answer = 0
    firstVal = ['0'] * len(ori)
    for i in range(len(firstVal)):
        if ori[i] != firstVal[i]:
            firstVal[i:] = ori[i] * len(firstVal[i:])
            answer+=1

    print("#{} {}".format(tc, answer))
