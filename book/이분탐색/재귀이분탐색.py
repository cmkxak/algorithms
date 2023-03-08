#재귀로 구현한 이진 탐색
import sys
input=sys.stdin.readline
def binary_search(start,end,array,target):
    if start > end:
        return None
    mid = (start + end)//2

    if array[mid] == target:
        return mid+1
    elif array[mid] < target: #중간 값의 위치 < 찾고자 하는 값 : 중간 값보다 오른쪽에 위치
        return binary_search(mid+1, end, array, target)
    else: # 중간 값의 위치 > 찾고자 하는 값 : 중간 값보다 왼쪽에 위치
        return binary_search(start, mid-1, array, target)

n,target=map(int, input().split())
array=list(map(int, input().split()))
result = binary_search(0, n - 1, array, target)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)