def solution(s):
    answer = True
    s = s.lower()
    p_count, y_count = 0,0
    
    for i in s:
        if i == 'p':
            p_count +=1
        elif i == 'y':
            y_count +=1
    if p_count == y_count or (p_count == 0 and y_count == 0):
        return True
    else:
        return False
    
    

    return True