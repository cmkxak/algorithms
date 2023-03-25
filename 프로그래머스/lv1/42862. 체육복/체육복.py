def solution(n, lost, reserve):
    answer =0
    #1. 전처리, 체육복을 가진 학생의 상태를 저장하는 student 배열 생성
    student= [0] * (n+2)

    #student 배열에 각 상태에 알맞은 숫자를 삽입
    for i in lost:
        student[i] -=1
    for i in reserve:
        student[i] +=1
    #이제 현재 상태에서 빌려줄 수 있는 경우를 모두 세주고, 체육에 참여할 수 있는 학생 수를 구한다.
    for i in range(1, n+1):
        if student[i] > 0:
            front = i-1
            back= i+1

            if student[front] < 0:
                student[i]-=1
                student[front]+=1

            elif student[back] < 0:
                student[i]-=1
                student[back]+=1
                
    for i in range(1,n+1):
        if student[i] >= 0:
            answer+=1
    return answer