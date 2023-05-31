p, m = map(int, input().split())
rooms = []

for i in range(p):
    lv, name = input().split()
    if not rooms:
        rooms.append([[int(lv), name]])
        continue
    for room in rooms:
        if len(room) < m and room[0][0] - 10 <= int(lv) <= room[0][0] + 10:
            room.append([int(lv), name])
            break
    else:
        rooms.append([[int(lv), name]])

for room in rooms:
    room.sort(key=lambda x : x[1])

for room in rooms:
    if len(room) == m:
        print("Started!")
        for idx,val in enumerate(room):
            print(room[idx][0], room[idx][1])
    else:
        print("Waiting!")
        for idx,val in enumerate(room):
            print(room[idx][0], room[idx][1])