import sys
input=sys.stdin.readline
n=input().rstrip()
list=[]
for i in n:
    list.append(i)
for i in range(len(list)):
    max_idx=i

    for j in range(i+1, len(list)):
        if list[j] > list[max_idx]:
            max_idx=j

    if list[max_idx] > list[i]:
        list[max_idx], list[i] = list[i], list[max_idx]

for i in list:
    print(i,end='')