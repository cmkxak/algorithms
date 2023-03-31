def solution(s):
    answer = len(s)
    
    for step in range(1, len(s) //2 + 1):
        compressed=""
        prev = s[:step]
        cnt=1
        for j in range(step, len(s), step):
            #이전 상태와 동일하다면 같은 것의 개수 증가
            if prev == s[j: j+step]:
                cnt+=1
            #이전 상태와 동일하지 않다면 압축을 진행하고 비교대상과 개수를 갱신 
            else:
                compressed+=str(cnt) + prev if cnt >=2 else prev
                prev = s[j: j+step]
                cnt=1
        
        #남은 문자열에 대해 처리
        compressed+= str(cnt) + prev if cnt >=2 else prev
        
        #만들어지는 압축 문자열이 가장 짧은 것이 정답 
        answer = min(answer, len(compressed))
    return answer