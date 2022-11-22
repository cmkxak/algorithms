#가장 긴 수열

# 수열의 크기 입력
# 크기 동안 수를 입력받음 , 중복 가능

# 가장 긴 증가하는 부분 수열 찾기.
# 중복 없이 수열의 합이 가장 큰 조합 찾기
# 가장 큰 조합이 나오는 경우, size 반환 하기

# sum 변수 초기화 떄리기
# ele가 sum보다 크거나 같으면 sum에 더해지도록 함
# 이 떄, count 증가

import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

sum = 0
answer = 0

for i in nums:
    if i >= sum:
        sum+=i
        answer+=1

print(answer)