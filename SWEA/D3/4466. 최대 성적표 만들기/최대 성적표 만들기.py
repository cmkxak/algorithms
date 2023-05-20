t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    total = 0
    for i in range(k):
        total+= scores[i]

    print("#{} {}".format(test_case, total))