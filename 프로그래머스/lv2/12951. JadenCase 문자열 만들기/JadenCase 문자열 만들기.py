def solution(s):
    list_s = s.split(" ")
    for i in range(len(list_s)):
        list_s[i]=list_s[i].capitalize()
    return ' '.join(list_s)