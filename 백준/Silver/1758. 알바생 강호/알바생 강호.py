n = int(input())
people = []
for i in range(n):
    people.append(int(input()))

people.sort(reverse=True)
tip = 0
for idx,val in enumerate(people):
    if val - ((idx+1)-1) < 0:
        continue
    tip += val - ((idx+1)-1)
print(tip)