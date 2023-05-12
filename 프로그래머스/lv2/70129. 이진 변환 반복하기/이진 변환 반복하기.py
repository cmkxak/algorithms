def solution(s):
    answer = []
    zero, cnt = 0,0
    while s != '1':
        zero += s.count('0')
        for i in s:
            if i == '0':
                s= s.replace(i, '')
        s = bin(len(s))[2:]
        cnt +=1
    answer.append(cnt)
    answer.append(zero)
    return answer