def solution(ingredient):
    answer = 0
    hamburger =[1,2,3,1]
    making = []
    for i in ingredient:
        making.append(i)
        
        if making[-4:] == hamburger:
            answer+=1
            for j in range(4):
                making.pop()
    
    return answer