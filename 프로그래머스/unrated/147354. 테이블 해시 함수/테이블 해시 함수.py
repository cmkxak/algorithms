def solution(data, col, row_begin, row_end):
    answer = 0
    
    #col번째 컬럼의 값을 기준으로 오름차순 정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    for i, val in enumerate(data):
        sum = 0
        if row_begin-1 <= i <= row_end-1:
            for j in val:
                sum += j % (i+1)
            answer ^= sum
    return answer
    
