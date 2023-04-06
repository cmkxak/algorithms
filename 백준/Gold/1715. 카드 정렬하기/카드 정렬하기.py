#카드 정렬하기
import heapq
import sys
input=sys.stdin.readline

n=int(input())
cards = []
new_cards,result = 0,0

for i in range(n):
    a=int(input())
    heapq.heappush(cards, a)

for i in range(len(cards)):
    if len(cards) == 1:
        break
    new_cards = heapq.heappop(cards) + heapq.heappop(cards)
    result+=new_cards
    heapq.heappush(cards, new_cards)

print(result)