n,m = map(int, input().split())
result = 0  

for i in range (n):
  cards = list(map(int, input().split()))
  min_val= min(cards)
  result= max(result, min_val)

print(result)
