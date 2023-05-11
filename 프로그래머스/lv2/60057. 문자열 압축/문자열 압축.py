def solution(s):
    result = len(s)
    for step in range(1,len(s)//2 + 1):
        cur = s[:step]
        answer=''
        cnt = 1
        for i in range(step, len(s), step):
            next = s[i : i + step]
            if cur == next:
                cnt+=1
            else:
                answer += str(cnt) + cur if cnt > 1 else cur
                cur = next
                cnt = 1
        answer+=str(cnt) + cur if cnt > 1 else cur
        result = min(result, len(answer))
    return result