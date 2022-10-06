#배열의 상, 하 반전
def calc1():
  temp = [[0] * m for _ in range(n)]
  for i in range(n):
    temp[i] = arr[n - 1 - i]
  return temp

#좌우 반전
def calc2():
	temp = [[0] * m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			temp[i][j] = arr[i][m - 1 - j]
	return temp

#오른쪽으로 90도 
def calc3():
  temp = [[0] * n for _ in range(m)]
  for i in range(m): #열의 개수 만큼 반복 ,3 
    for j in range(n): #행의 개수 만큼 반복, 2 
      temp[i][j] = arr[n-1-j][i] 
  return temp

#왼쪽으로 90도
def calc4():
	temp = [[0] * n for _ in range(m)]
	for i in range(m):
		for j in range(n):
			temp[i][j] = arr[j][m - 1 - i] ## 
	return temp

def calc5():
	print(1)


def calc6():
	print(1)


n, m, count = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

operation = list(map(int, input().split()))

for oper in operation:
	if oper == 1:
		arr = calc1()
	elif oper == 2:
		arr = calc2()
	elif oper == 3:
		arr = calc3()
	elif oper == 4:
		arr = calc4()
	elif oper == 5:
		arr = calc5()
	elif oper == 6:
		arr = calc6()

for i in arr:
	print(*i, sep = ' ')
