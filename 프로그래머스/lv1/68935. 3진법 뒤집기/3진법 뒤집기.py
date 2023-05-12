def change(n):
    answer = ''
    while n>=1:
        answer+= str(n%3)
        n//=3
    return answer


def solution(n):
    answer = 0
    changedNum = change(n)
    answer = int(changedNum, 3)
    return answer