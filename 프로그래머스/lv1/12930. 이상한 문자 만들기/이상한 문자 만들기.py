def solution(s):
    answer = ''
    tmp=[]
    list_s=s.split(" ")
    for val in list_s:
        for i in range(len(val)):
            if i % 2 == 0:
                answer+=val[i].upper()
            elif i % 2 != 0:
                answer+=val[i].lower()
        tmp.append(answer)
        answer=''
    print(" ".join(tmp))
    return " ".join(tmp)