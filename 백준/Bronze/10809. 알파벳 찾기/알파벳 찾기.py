s=input()
answer = []
for i in range(97, 123):
    if chr(i) in s:
        answer.append(list(s).index(chr(i)))
    else:
        answer.append(-1)
for i in answer:
    print(i, end=' ')