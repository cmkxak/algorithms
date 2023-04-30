def solution(phone_number):
    answer = ''
    answer+= '*' * (len(phone_number) - 4) + str(phone_number[len(phone_number) -4:])
    return answer