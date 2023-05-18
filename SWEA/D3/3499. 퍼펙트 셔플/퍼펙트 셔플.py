t=int(input())
for tc in range(1, t+1):
    n = int(input())
    cards = list(input().split())
    answer = []
    if n % 2 == 0:
        cards1, cards2 = cards[:n//2], cards[n//2:]
        for i in range(len(cards1)):
            answer.append(cards1[i])
            answer.append(cards2[i])
    else:
        cards1, cards2 = cards[:n//2+1], cards[n//2+1:]
        for i in range(len(cards2)):
            answer.append(cards1[i])
            answer.append(cards2[i])
        answer.append(cards1[-1])
    print("#{} {}".format(tc, ' '.join(answer)))
