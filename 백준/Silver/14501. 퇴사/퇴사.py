def find_max_benefit(day, price):
    global max_benefit
    if day == n:
        if max_benefit < price:
            max_benefit = price
        return
    #상담을 해줄 수 있는 경우
    if day + int(L[day][0]) <= n:
        find_max_benefit(day+int(L[day][0]), price+int(L[day][1]))
    #상담을 안받는 경우
    find_max_benefit(day+1, price)

n = int(input())
L = [input().split() for _ in range(n)]
max_benefit=0
find_max_benefit(0,0)
print(max_benefit)
