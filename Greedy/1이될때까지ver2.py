n,k = map(int, input().split())
count = 0

while True:
  #나누어 떨어지는 수로 될때까지 1씩 빼기
  target = (n//k) * k
  count+= (n-target)
  n = target
  #n이 K보다 작을 때(더이상 나눐 수 없을 때) 반복문 탈출
  if n<k:
    break
  #K로 나누기
  count+=1
  n//=k

#마지막으로 남은 수에 대하여 1씩 빼기
count= count + (n-1)
print(count)
