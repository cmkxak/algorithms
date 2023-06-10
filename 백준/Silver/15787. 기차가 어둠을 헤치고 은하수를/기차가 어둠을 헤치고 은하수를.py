import copy

n,m = map(int, input().split())

train = [[0] * 20 for i in range(n)]
answer=  []
for _ in range(m):
    orders = list(map(int, input().split()))

    #명령에 따라 행위를 결정한다.
    if orders[0] == 1:
        train[orders[1]-1][orders[2]-1] = 1 #승객 승차
    #하차
    elif orders[0] == 2:
        train[orders[1]-1][orders[2]-1] = 0 #승객 하차

    #뒤로 한칸씩 미뤄줌
    elif orders[0] == 3:
        prev = copy.deepcopy(train[orders[1]-1])
        for i in range(19):
            train[orders[1]-1][i+1] = prev[i]
        train[orders[1]-1][0] = 0 #첫번째 구간 0으로 초기화

    #앞으로 한칸씩 미뤄줌
    else:
        prev = copy.deepcopy(train[orders[1]-1])
        for i in range(1,20):
            train[orders[1]-1][i-1] = prev[i]
        train[orders[1]-1][19] = 0
for i in train:
    if i not in answer:
        answer.append(i)
print(len(answer))