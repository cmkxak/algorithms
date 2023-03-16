cur=input()
row=int(cur[1])
col=ord(cur[0]) - ord('a') + 1
cnt=0
move_type=[[-2,-1], [-2,1], [2,1], [2,-1], [1,-2], [-1,-2], [-1,2], [1,2]]
for i in move_type:
    nx= row + i[1]
    ny= col + i[0]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    cnt+=1
print(cnt)