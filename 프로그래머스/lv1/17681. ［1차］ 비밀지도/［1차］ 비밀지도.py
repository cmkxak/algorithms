def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr1[i] = '0' * (n - len(bin(arr1[i])[2:])) + bin(arr1[i])[2:]
    for i in range(len(arr2)):
        arr2[i] = '0' * (n- len(bin(arr2[i])[2:])) + bin(arr2[i])[2:]
    for i in range(len(arr1)):
        tmp = ''
        for j in range(len(arr2)):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                tmp+='#'
            elif arr1[i][j] == '0' and arr2[i][j] == '0':
                tmp+=' '
        answer.append(tmp)
    return answer