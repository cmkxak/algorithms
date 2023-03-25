def solution(n, lost, reserve):
    reserve_stu = set(reserve) - set(lost)
    lost_stu = set(lost) - set(reserve)
    
    #빌려줄 수 있는 학생을 기준으로 최대한 많이 빌려준다.
    for i in reserve_stu:
        front = i-1
        back = i+1

        if front in lost_stu:
            lost_stu.remove(front)
        elif back in lost_stu:
            lost_stu.remove(back)
    print(n-len(lost_stu))
    return n - len(lost_stu)