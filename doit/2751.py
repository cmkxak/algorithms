import sys
input = sys.stdin.readline

n = int(input())
list = []

for i in  range(n):
    num = int(input())
    list.append(num)

list.sort()

for i in list:
    print(i)
