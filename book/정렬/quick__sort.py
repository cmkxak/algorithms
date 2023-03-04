# 퀵 정렬
nums=[42,32,24,60,15,5,90,45]
s=0
e=len(nums)-1
pivot=len(nums)

while s<e:
    #피봇이 가리키는 데이터 > 왼쪽 포인터가 가리키는 데이터
    if nums[pivot] > nums[s]:
        s+=1
    elif nums[pivot] < nums[e]:
        e-=1
    else:
        nums[s], nums[e] = nums[e], nums[s]
        s+=1
        e-=1