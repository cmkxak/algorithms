import sys
input = sys.stdin.readline
n = int(input())
per = list(map(int, input().split()))

def bnp(money):
    count = 0
    for i in per:
        #주가 > 보유 현금
        if i <= money:
            count+= (money // i)
            money = money % i
    return (count * per[13]) + money

def threethree(money):
    count = 0
    downCnt = 0
    upCnt = 0
    for i in range(len(per)):
        # 주가가 하락한 경우
        if per[i-1] > per[i]:
            downCnt+=1
            upCnt = 0
        # 주가가 상승한 경우
        elif per[i-1] < per[i]:
            upCnt+=1
            downCnt = 0
        # 주가가 전날과 동일한 경우
        else:
            upCnt,downCnt = 0,0
        # 주가 <= 보유 현금 && 하락일이 연속 3일째가 되면
        if per[i] <= money and downCnt >= 3:
            #전량 매수
            count+= money // per[i]
            money = money % per[i]
        #주가 <= 보유 현금 && 상승일이 연속 3일째가 되면
        if per[i] <= money and upCnt >=3:
            #전량 매도
            money += (count * per[i])
            count = 0 #보유 주식 초기화

    return money + (count * per[13])

if bnp(n) > threethree(n):
    print("BNP")
elif bnp(n) < threethree(n):
    print("TIMING")
else:
    print("SAMESAME")
