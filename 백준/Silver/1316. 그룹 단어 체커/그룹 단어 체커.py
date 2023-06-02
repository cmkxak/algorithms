n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)

cnt = n
for word in words:
    memo = [word[0][0]]
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            memo.append(word[i])
            continue
        else:
            if word[i+1] not in memo:
                memo.append(word[i+1])
            else:
                cnt-=1
                break
print(cnt)