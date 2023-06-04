def solution(book_time):
    answer = 0
    
    book_time = sorted(book_time, key=lambda x: x[0])
    
    reserve_last_time = 0
    
    print(book_time)
    
    rooms = [[reserve_last_time]]
    
    for time in book_time:
        time[0] = time[0].split(':')
        time[1] = time[1].split(":")
        
        reserve_start_time = int(time[0][0]) * 60  + int(time[0][1])
        finish_time = int(time[1][0]) * 60 + int(time[1][1]) + 10 
        
        for room in rooms:
            if reserve_start_time >= room[0]:
                room[0] = finish_time
                break
            else:
                continue
        else:
            rooms.append([finish_time])
    return len(rooms)