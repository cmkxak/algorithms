def solution(s):
cnt_bin = 0
cnt_zero = 0

while True:
    if s == '1':
        break
    cnt_zero+=s.count('0') #0의 개수를 더해줌
    cnt_bin +=1 # 이진 변환 횟수 더함

    s = s.replace('0','') #문자열 1만 남게 변경
    s = bin(len(s))[2:] # 이진 변환 결과로 초기화
return [cnt_bin, cnt_zero]

# 다른사람은 직접 구현함 -> 2진수 // bin
#
# def makeBin(len):
#     result = []
#     while len != 0:
#         if len % 2 == 1:
#             result.append("1")
#             len = (len-1)/2
#         else:
#             result.append("0")
#             len = len/2
#     return result
#
# def solution(s):
#     answer = []
#     x = s[:]
#     zero_count = 0
#     itr_count = 0
#     if x == "1":
#         answer = [0, 0]
#     else:
#         while x != "1":
#             temp = []
#             itr_count += 1
#             for i in x:
#                 if i == "1":
#                     temp.append("1")
#                 else:
#                     zero_count += 1
#             x = "".join(makeBin(len(temp)))
#     answer = [itr_count, zero_count]
#     return answer