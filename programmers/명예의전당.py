def solution(k, score):
    answer = []
    honor = []
    for i in score:
        if len(honor) >= k:
            if min(honor) < i:
                honor.remove(min(honor))
                honor.append(i)
        else:
            honor.append(i)
        answer.append(min(honor))

    return answer