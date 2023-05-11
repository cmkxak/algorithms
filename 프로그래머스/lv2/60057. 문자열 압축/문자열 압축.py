def solution(s):
    answer = ''
    
    for step in range(len(s)//2 + 1):
        cur = s[:step]
        cnt = 0
        for i in range(step+1, len(s)):
            if cur == s[i:]:
                cnt+=1
            else:
                answer += str(cnt) + s[i] if cnt > 0 else s[i:]
                cur = s[i]
                cnt = 0
    return answer