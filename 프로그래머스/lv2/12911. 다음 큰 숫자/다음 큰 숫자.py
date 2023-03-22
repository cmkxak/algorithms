def solution(n):
    answer = 0
    bin_n=bin(n)[2:]
    cnt_one = bin_n.count('1')
    while True:
        n+=1
        if bin(n)[2:].count('1') == cnt_one:
            answer = n
            break
    return answer