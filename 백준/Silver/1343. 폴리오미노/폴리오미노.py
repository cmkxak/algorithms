s = input()
idx = 0
answer = ''

while idx<len(s):
    if s[idx : idx + 4] == 'XXXX':
        answer+='AAAA'
        idx+=4
    elif s[idx : idx + 2] == 'XX':
        answer += 'BB'
        idx+=2
    elif s[idx] == 'X':
        answer = str(-1)
        break
    else:
        answer += s[idx]
        idx+=1
print(answer)