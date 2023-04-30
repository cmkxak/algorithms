def solution(s, n):
    answer = ''
    #어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을
    #시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다.
    #z는 1만큼 밀면 "a"가 됩니다.
    for i in s:
        if i == ' ':
            answer += i
        #소문자인 경우
        if ord('a') <= ord(i) <= ord('z'):
            if ord(i) + n > ord('z'):
                answer += chr(ord(i) - 26  + n)
            else:
                answer += chr(ord(i) + n)
        #대문자인 경우
        if ord('A') <= ord(i) <= ord('Z'):
            if ord(i) + n > ord('Z'):
                answer += chr(ord(i) - 26 + n)
            else:
                answer += chr(ord(i) + n)
    return answer