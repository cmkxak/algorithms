a,b,c = map(int, input().split())
info = [0] * 101
for i in range(3):
    s,e = map(int, input().split())
    for j in range(s, e):
        info[j] += 1
sum = 0
for i in range(len(info)):
    if info[i] == 1:
       sum += a
    elif info[i] == 2:
        sum += (2 * b)
    elif info[i] == 3:
        sum += (3 * c)
print(sum)