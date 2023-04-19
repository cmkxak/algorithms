def solution(n):
    answer = ''
    
    nums = ['1','2','4']
    while n>0:
        n-=1 #3
        answer = nums[n%3] + answer
        print(answer,len(answer))
        n//=3 #1
    
    return answer