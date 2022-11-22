n = int(input()) # 재료의 개수
M = int(input()) # 재료를 만드는데 필요한 수
nums = list(map(int, input().split()))
start_idx = 0
end_idx = n-1
count = 0
nums.sort()

while start_idx < end_idx:
    if nums[start_idx] + nums[end_idx] == M:
        count+=1
        start_idx+=1
        end_idx-=1
    #작으면 큰 값으로 인덱스르 밀어준다
    elif nums[start_idx] + nums[end_idx] < M:
        start_idx+=1
    #크면 작은 값으로 인덱스를 밀어준다
    else:
        end_idx-=1

print(count)