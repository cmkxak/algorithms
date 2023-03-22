def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if answer:
        return sorted(answer)
    else:
        answer.append(-1)
        return answer
