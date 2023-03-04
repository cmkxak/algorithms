#주몽의 명령
N=int(input()) #재료수
M=int(input()) #갑오승ㄹ 만드는데 필요한 수
ingredi_nums=list(map(int, input().split()))
ingredi_nums.sort()
s_idx=0
e_idx=len(ingredi_nums)-1
count=0

while s_idx < e_idx:
    if ingredi_nums[s_idx] + ingredi_nums[e_idx] < M:
        s_idx+=1
    elif ingredi_nums[s_idx] + ingredi_nums[e_idx] > M:
        e_idx-=1
    else:
        count+=1
        s_idx+=1
        e_idx-=1
print(count)