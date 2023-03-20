def solution(n):
    answer=''
    list_n=list(str(n))
    list_n.sort(reverse=True)
    for i in list_n:
        answer+=i
    return int(answer)