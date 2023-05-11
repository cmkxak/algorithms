answer = ''
def getCurrent(number,graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == number:
                return (i,j)

def calculateAnswer(graph,left_s, right_s,numbers,hand):
    global answer
    left_c = [1,4,7]
    right_c = [3,6,9]

    for number in numbers:
        if number in left_c:
            answer+='L'
            left_s = getCurrent(number,graph)
        elif number in right_c:
            answer+='R'
            right_s = getCurrent(number,graph)
        else:
            cur = getCurrent(number,graph)
            left_dist = abs(cur[0] - left_s[0]) + abs(cur[1] - left_s[1])
            right_dist = abs(cur[0] - right_s[0]) + abs(cur[1] - right_s[1])
            if left_dist == right_dist:
                if hand == "right":
                    answer+='R'
                    right_s = getCurrent(number, graph)
                else:
                    answer+='L'
                    left_s = getCurrent(number,graph)
            else:
                if left_dist<right_dist:
                    answer+='L'
                    left_s = getCurrent(number, graph)
                else:
                    answer+='R'
                    right_s = getCurrent(number, graph)

def solution(numbers, hand):
    pad = [1,2,3,4,5,6,7,8,9,99,0,100]
    graph = [[0] * 3 for i in range(4)]

    idx=0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            graph[i][j] = pad[idx]
            idx+=1

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 99:
                left_s = (i,j)
            elif graph[i][j] == 100:
                right_s = (i,j)
    calculateAnswer(graph, left_s, right_s, numbers, hand)
    return answer