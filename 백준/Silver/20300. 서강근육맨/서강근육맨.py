n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
tmp = []
if n % 2 != 0:
    tmp.append(data.pop(0))
for i in range(n//2):
    tmp.append(data[i] + data[-i-1])
print(max(tmp))