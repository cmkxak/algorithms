# 투 포인터 활용 문제
n = int(input())
start_idx = 1
end_idx = 1
count = 1
sum = 1

while end_idx != n:
    # sum값과 입력 수가 같은 경우
    if sum == n:
        count+=1
        end_idx +=1
        sum+=end_idx

    elif sum > n:
        sum-=start_idx
        start_idx+=1

    else:
        sum+=end_idx
        end_idx+=1
print(count)