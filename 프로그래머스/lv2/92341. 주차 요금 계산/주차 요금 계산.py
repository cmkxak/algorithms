import math

def getMinute(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1]) 

def getFee(carNum, time,fees):
    if time > fees[0]:
        return fees[1] + math.ceil(max(0, (time - fees[0]) / fees[2])) * fees[3]
    else:
        return fees[1]
    
def solution(fees, records):
    answer = []
    parking = dict()
    parkingAllInfo = dict()
    for record in records:
        record = record.split(" ")
        minute = getMinute(record[0])
        
        #IN이면 시간 초기화
        if record[2] == 'IN':
            parking[record[1]] = minute
        
        #OUT이면 누적 시간 갱신
        elif record[2] == 'OUT':
            #누적 정보 = 현재 시간 - 시작 시간
            try:
                parkingAllInfo[record[1]] += (minute - parking[record[1]])
            except:
                parkingAllInfo[record[1]] = minute - parking[record[1]]
            del parking[record[1]]
    
    for key,value in parking.items():
        try:
            parkingAllInfo[key] += getMinute("23:59") - value
        except:
            parkingAllInfo[key] = getMinute("23:59") - value
            
    
    for key, value in sorted(parkingAllInfo.items(), key=lambda x: x[0]):
        answer.append(getFee(key, value,fees))
    return answer