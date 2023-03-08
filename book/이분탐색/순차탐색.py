def sequential_search(n,target,array):
    #각 원소를 하나씩 탐색하면서
    for i in range(int(n)):
        #현재의 원소가 찾고자 하는 원소와 동일한 경우
        if target == array[i]:
            return i+1 #현재의 위치 반환 (idx는 0부터 시작하므로 1더하기)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
n,target=input().split()

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array=input().split()
print(sequential_search(n,target,array))