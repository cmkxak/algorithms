data = input()
#파이썬 : 문자열의 특정 인덱스의 값을 배열인덱스 마냥 접근 가능 
result = int(data[0])

for i in range(1,len(data)):
  num = int(data[i])
  if num<=1 or result <=1:
    result+=num
  else:
    result*=num
    
print(result)