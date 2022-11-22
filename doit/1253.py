import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
good_count = 0
nums.sort()


for k in range(n):
    find = nums[k]
    #k값이 변경될 경우에 i,j 값을 다시 초기화해서 사용해야 한다.
    i = 0
    j = n-1

    while i < j:
        if nums[i] + nums[j] == find:
            if i != k and j != k: #서로 다른 수의 합이어야 하므로 k와 같지 않을 때를 고려해준다.
                good_count+=1 # 좋은 수 개수 증가
                break
            elif i == k: 
                i+=1
            elif j == k:
                j-=1
        elif nums[i] + nums[j] < find:
            i+=1
        else:
            j-=1

print(good_count)

