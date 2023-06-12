n = int(input())

schedule = [0] * 366
for i in range(n):
    s, e = map(int, input().split())

    for i in range(s, e+1):
        schedule[i] += 1
row = col = answer = 0

#이제 생각한 아이디어 대로 직사각형을 만든다 혹은 만들지 않고 변수 값들을 초기화 해간다.
for i in range(len(schedule)):
    if schedule[i] != 0:
        row = max(row, schedule[i])
        col += 1
    else:
        answer += row * col
        row = 0
        col = 0
answer += row * col
print(answer)