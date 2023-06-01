from itertools import combinations

L,C = map(int, input().split())

candidates = list(input().split())
password = []

for pw in combinations(candidates, L):
    pw = sorted(pw)
    password.append(pw)

password.sort()
for pw in password:
    cnt = alphabet = 0
    for p in pw:
        if p in ['a','e','i','o','u']:
            cnt += 1
        else:
            alphabet += 1
    if alphabet >= 2 and cnt >= 1:
        print(''.join(pw))