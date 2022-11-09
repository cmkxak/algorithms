#이진 탐색을 하기 전에는 반드시 자료를 미리 정렬해야 한다.
def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] > x:
            end = mid - 1
        elif a[mid] < x:
            start = mid + 1
        elif a[mid] == x:
            return 1
    return 0


n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
nums = list(map(int, input().split()))

for i in range(m):
    #이진 탐색 대상 배열과 비교할 값을 가진 배열의 길이만큼 비교한다.
    print(binary_search(a, nums[i]))
