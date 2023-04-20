def solution(s):
    l_s=list(s)
    print(l_s)
    if len(l_s) % 2 == 0:
        return ''.join(l_s[len(s)//2 -1: len(s)//2 + 1])
    else:
        return ''.join(l_s[len(s)//2])