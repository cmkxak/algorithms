import sys
input = sys.stdin.readline

n,m = map(int, input().split())

money = list(map(int, input().split()))

salary = sum(money[:m])
answer= salary

for i in range(m, n):
    salary += money[i] - money[i-m]
    answer = max(salary, answer)
print(answer)