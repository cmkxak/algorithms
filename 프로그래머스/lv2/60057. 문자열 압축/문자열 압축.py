#압축하여 표현한 문자열 중 가장 짧은 것의 길이를 리턴하도록 솔루션 함수를 완성해라.
def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2 + 1):
        cur = s[:step] 
        cnt = 1
        tmp = ''
        for j in range(step, len(s), step):
            next = s[j:j+step]
            if cur == next:
                cnt+=1            
            else:
                tmp+= (str(cnt) + cur) if cnt>=2 else cur
                cur = next
                cnt=1
        tmp+=str(cnt) + cur if cnt>=2 else cur #마지막 문자열 더해줌
        answer = min(answer, len(tmp))
    return answer