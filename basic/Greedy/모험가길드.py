n = int(input())
data = list(map(int, input().split()))
data.sort() #공포도 데이터 값 오름차순 정렬

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수 

for d in data:
  count+=1 #현재 그룹에 해당 모험가를 포함 시키기
  if count >= d: #현재 그룹에 포함된 모험가의 수 >= 공포도이면 그룹 결성
    result+=1 #총 그룹의 수 증가
    count = 0 #현재 그룹에 포함된 모험가의 수 초기화

print(count) # 총 그룹의 수 출력
     