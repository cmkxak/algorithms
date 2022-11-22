def solution(left, right):
    answer = 0
    y = 1
    for i in range(left, right+1):
        for j in range(1,i//2+1):
            if i%j == 0:
                y+=1
        if y % 2 == 0:
            answer+=i
        else:
            answer-=i
        y=1 #디버깅 통해 알아낸 문제, i가 변경되더라도 y(약수의 개수)가 계속 누적되는 현상 발생, 따라서 하나의 수를 비교할 때마다 갱신
    return answer