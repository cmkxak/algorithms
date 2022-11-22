n = int(input())
list = [int(input()) for i in range(n)]

temp = 0

for i in range(n-1):
    for j in range(n-1-i): #이미 정렬된 마지막 부분은 제외
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

for i in range(n):
    print(list[i])