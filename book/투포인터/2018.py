import sys
input=sys.stdin.readline
n=int(input()) # n을 입력받는다.
s_idx,e_idx=1,1
sum,cnt=1,1
#end_idx가 n과 같지 않을 때 까지 반복한다.
while e_idx != n:
    # n이 합보다 큰 경우
    if sum < n:
        e_idx+=1 # 연속된 자연수의 범위를 한칸 더 확장
        sum+=e_idx
    #합이 n보다 큰 경우
    #작은 값을 뺴주면서 합의 값이 구하고자 하는 n값에 가까워지도록 접근한다.
    elif sum>n:
        sum-=s_idx
        s_idx+=1
    #합과 n이 같은 경우
    #경우의 수를 하나 증가하고, end_idx를 증가한다.
    else:
        cnt+=1
        e_idx+=1
        sum+=e_idx
print(cnt)
