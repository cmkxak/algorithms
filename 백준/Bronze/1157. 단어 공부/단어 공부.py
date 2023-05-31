words = input().upper()
#입력받은 문자열에서 중복값을 제거
unique_words = list(set(words))

cnt_list = []
for x in unique_words:
    #원래 문자열에서 각 알파벳들이 몇 개인지 count 해준다.
    cnt = words.count(x)
    #count 숫자를 리스트에 append
    cnt_list.append(cnt)

#알파벳 개수가 가장 큰 것이 여러개이면
if cnt_list.count(max(cnt_list)) > 1:
    print("?")

#그렇지 않으면, 가장 많이 사용된 알파벳을 대문자로 출력 
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])
