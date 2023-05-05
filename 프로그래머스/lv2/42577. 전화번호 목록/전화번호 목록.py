def solution(phone_book):
    answer = True
    
    phone_dict ={}
    
    for i, phone in enumerate(phone_book):
        phone_dict[phone] = i
    
    for phone in phone_book:
        tmp = ''
        for p in phone:
            tmp+=p
            if tmp in phone_dict.keys() and phone != tmp:
                answer = False
                break
    return answer