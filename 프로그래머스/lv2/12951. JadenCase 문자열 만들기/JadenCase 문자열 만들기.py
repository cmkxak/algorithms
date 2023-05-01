def solution(s):
    s= s.split(' ')
    answer = ''
    for i in s:
        answer+= ' ' + i.capitalize()
    print(answer)
    return answer[1:]