def solution(arr):
    answer = max(arr)
    cnt=0
    while True:
        for i in range(len(arr)):
            if answer % arr[i] == 0:
                cnt+=1
            else:
                cnt=0
                answer+=1
                break
        if len(arr) == cnt:
            return answer