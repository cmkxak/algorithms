import sys
input=sys.stdin.readline

def binary_search(array, target):
    start = 0
    end=len(array)-1
    while start<=end:
        mid=(start+end)//2

        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end=mid-1
        else:
            start=mid+1
    return "no"

n=int(input())
machines=list(map(int, input().split()))
machines.sort()
k=int(input())
customers=list(map(int, input().split()))
for i in range(k):
    print(binary_search(machines, customers[i]), end=' ')