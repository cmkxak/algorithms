from collections import Counter

def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    
    #2글자씩 끊어서 다중 집합의 원소로 만든다.
    str1_candidates,str2_candidates = [],[]
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_candidates.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_candidates.append(str2[i] + str2[i+1])
    
    counter_str1 = Counter(str1_candidates)
    counter_str2 = Counter(str2_candidates)
    
    inter = list((counter_str1 & counter_str2).elements())
    union = list((counter_str1 | counter_str2).elements())
    
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int((len(inter)/len(union)) * 65536)
