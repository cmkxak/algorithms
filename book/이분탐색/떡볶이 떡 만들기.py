import sys
input=sys.stdin.readline
def binary_search(array,target_amount):
    start=0
    end=max(array)

    while start<=end:
        sum=0
        mid=(start+end)//2

        #떡의 잘린 갯수를 구해준다.
        for i in array:
            if i > mid:
                sum+=i-mid

        #타겟보다 더 많이 잘렸으면, 높이가 낮은 것
        if sum > target_amount:
            start=mid+1
        elif sum < target_amount:
            end=mid-1
        else:
            return mid

n,m = map(int,input().split())
breads = list(map(int,input().split()))
print(binary_search(breads,m))