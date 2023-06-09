#시작 문자열 입력
l_start, r_start = input().split()
#탐색 할 문자열 입력
alphabet = input()
#자음 리스트
left_list = ['q','w','e','r', 't', 'a', 's', 'd','f','g', 'z', 'x', 'c', 'v']
#모음 리스트
right_list = ['y','u','i','o','p','h','j','k','l', 'b', 'n', 'm']

#현재 주어진 키보드 형태
keyboard = [
    ['q','w','e','r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a','s', 'd','f','g','h','j','k','l'],
    ['z','x', 'c', 'v','b', 'n', 'm']
]

#자음을 누르는 손가락 위치
lx,ly = 0,0
#모음을 누르는 손가락 위치
rx,ry = 0,0

#거리 계산을 위한 변수
cnt = 0

#시작점 초기화
for i in range(len(keyboard)):
    if l_start in keyboard[i]:
        lx = i
        ly = keyboard[i].index(l_start)

    if r_start in keyboard[i]:
        rx = i
        ry = keyboard[i].index(r_start)

#문자를 하나씩 읽으면서 거리 계산 및 키보드 누르는 시간을 계산해준다.
for keyword in alphabet:
    if keyword in right_list:
        for i in range(len(keyboard)):
            if keyword in keyboard[i]:
                nx = i
                ny = keyboard[i].index(keyword)

                cnt += abs(rx - nx) + abs(ry - ny) + 1
                rx,ry = nx,ny
                break
    else:
        for i in range(len(keyboard)):
            if keyword in keyboard[i]:
                nx = i
                ny = keyboard[i].index(keyword)

                cnt += abs(lx - nx) + abs(ly - ny) + 1
                lx, ly = nx, ny
                break
print(cnt)