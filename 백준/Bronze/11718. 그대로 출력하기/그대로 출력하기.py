while True:
    #몇번의 입력이 있는지 주어지는 경우가 보통 대다수지만, 이번 문제의 경우 몇번의 입력이 있었는지 전혀 주어지지 않았음
    #따라서 try Catch문으로 에러 발생 시 탈출 설정
    try:
        n=input()
        print(n)
    except EOFError:
        break

