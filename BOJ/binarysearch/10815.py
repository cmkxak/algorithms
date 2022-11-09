def binary_search(a, x):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] > x:
            end = mid - 1
        elif a[mid] < x:
            start = mid + 1
        elif a[mid] == x:
            return 1
    return 0

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
givenCard = list(map(int, input().split()))

for i in range(m):
    print(binary_search(card, givenCard[i]), end = ' ')
