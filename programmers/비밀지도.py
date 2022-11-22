def solution(n, arr1, arr2):
    answer = []
    graph = []
    graph2 = []
    # 2진 변환 한 수에 0을 찍어줘야 하는데, 전체 길이에서 2진수로 변환한 값의 길이를 뺴주면 그게 0의 개수이므로 아래와 같이 표현
    for i in range(n):
        graph.append(bin(arr1[i])[2:])
        graph2.append(bin(arr2[i])[2:])

        graph[i] = ('0' * (n-len(graph[i]))) + graph[i]
        graph2[i] = ('0' * (n-len(graph2[i]))) + graph2[i]

        temp= ''
        # 하나씩 값을 다 보면서 지도에서 둘 중 하나라도 1이면 # 그렇지 않으면 0
        for p in range(n):
            if graph[i][p] == '1' or graph2[i][p] == '1':
                temp+='#'
            elif graph[i][p] == '0' or graph2[i][p] == '0':
                temp+=" "
        answer.append(temp)
    return answer
# 다른 사람 풀이
def solution(n , arr1, arr2):
    answer = []
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])[2:n].zfill(n).replace('1', '#').replace('0', ' ')
        answer.append(tmp)
    return answer