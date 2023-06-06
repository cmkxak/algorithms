#key랑 타겟 비교하는게 핵심 로직 
'''
현재 내 버전 : 키맵에서 키를 하나씩 꺼내서 같으면 인덱스 가져옴
각각의 키 버튼에서 가장 작은 버튼을 누르는 횟수를 인덱스를 통해 구해줌
'''
    
def solution(keymap, targets):
    answer = []
    for target in targets:
        result = 0
        for t in target:
            cnt = 101
            isPushed = False
            for key in keymap:
                if t in key:
                    cnt = min(key.index(t)+1, cnt)
                    isPushed = True
            if not isPushed:
                result = -1
                break
            result += cnt
        answer.append(result)
    return answer