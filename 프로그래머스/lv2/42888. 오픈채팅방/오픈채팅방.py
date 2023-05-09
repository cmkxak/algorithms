def solution(record):
    answer = []
    memoryDB = {}
    
    for idx, r in enumerate(record):
        userInfo = r.split(' ')
        
        if userInfo[0] != "Leave":
            order, userId, userName = userInfo[0], userInfo[1], userInfo[2] 
            memoryDB[userId] = userName
            
        if userInfo[0] in ["Enter", "Leave"]:
            order, userId = userInfo[0], userInfo[1]
            answer.append((userId, order))
    for idx, val in enumerate(answer):
        if val[1] == "Enter":
            answer[idx] = memoryDB[val[0]] + "님이 들어왔습니다."
        elif val[1] == "Leave":
            answer[idx] = memoryDB[val[0]] + "님이 나갔습니다."
    return answer