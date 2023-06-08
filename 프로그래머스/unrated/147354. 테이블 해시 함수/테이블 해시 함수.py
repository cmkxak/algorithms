def solution(data, col, row_begin, row_end):
    answer = 0
    
    #col번째 컬럼의 값을 기준으로 오름차순 정렬
    data.sort(key=lambda x: x[0], reverse=True)
    data.sort(key=lambda x : x[col-1])
    
    sumList = []
    for i, val in enumerate(data):
        sum = 0
        for j in val:
            sum += j % (i+1)
        sumList.append(sum)
    print(sumList)
    
    for i in range(row_begin-1, row_end):
        answer ^= sumList[i]
        print(answer)
    return answer
    
