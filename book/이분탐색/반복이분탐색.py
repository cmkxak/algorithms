import sys
input=sys.stdin.readline

def binary_search(start, end, array, target):
    while start <= end:
        mid = (start + end) // 2

        #중간점의 데이터 < 찾고자 하는 데이터
        if array[mid] < target:
            start = mid+1
        #중간점의 데이터 > 찾고자 하는 데이터
        elif array[mid] > target:
            end = mid-1
        #중간점의 데이터 = 찾고자 하는 데이터
        else:
            return mid + 1
    return "원소가 존재하지 않습니다."
n,target = map(int, input().split())
array=list(map(int, input().split()))
print(binary_search(0,n-1, array, target))