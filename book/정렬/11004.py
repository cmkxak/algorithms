# 오름 차순 정렬 - 퀵 정렬
# k 번째에 있는 수를 구하라.
import sys
input=sys.stdin.readline
n,k=map(int, input().split())
nums=list(map(int, input().split()))

def quick_sort(s,e,k):
    pivot = partition(s,e)

    if pivot == k: #k번째 수가 pivot 이면 더 이상 구할 필요 없음
        return
    elif pivot > k: #k번째 수가 pivot보다 작은 경우 (왼쪽만 탐색하면 됨.)
        return quick_sort(s, pivot, k)
    else: #k번째 수가 pivot 보다 큰 경우 (오른쪽만 탐색하면 됨.)
        return quick_sort(pivot+1,e,k)

def partition(s,e):
    #남은 원소가 두개일 경우
    if s+1==e:
        if nums[s] > nums[e]:
            nums[s],nums[e] = nums[e],nums[s]
        return e

    mid=(s+e)//2
    nums[mid], nums[s] = nums[s], nums[mid]
    #피봇값 맨 앞으로 고정
    pivot=nums[s]

    #시작점, 끝점 지정
    i=s+1
    j=e

    #시작점이 끝점보다 작거나 같은 동안 반복한다.
    while i<=j:
        #피봇이 가리키는 값 > i가 가리키는 값
        while pivot > nums[i] and i < len(nums)-1:
            i+=1
        #피봇이 가리키는 값 < j가 가리키는 값
        while j > 0 and pivot < nums[j]:
            j-=1

        if i<=j:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
            j-=1

    #결국 j의 위치가 피봇의 위치가 될 것임.
    #따라서 피봇의 값을 가지고 있는 첫번쨰와 j번쨰의 값을 swap 해준다.
    nums[s] = nums[j]
    nums[j] = pivot
    return j

quick_sort(0, n-1, k-1)
print(nums[k-1])
