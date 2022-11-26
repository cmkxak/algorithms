# # 기본 구조
# _list = [i for i in range(10)]
# print(_list) #[0,1,2,3,4,5,6,7,8,9]
import random

#예제 이해하기 - BOJ 1920번
# import sys
# input = sys.stdin.readline
#
# _ = input()
# _set = set(map(int, input().split()))
# q = input()
# _list = list(map(int, input().split()))
#
# print(*[1 if dt in _set else 0 for dt in _list], sep='\n')

#다차원 배열을 짜보자.
_list2 = [[(i+1)**2 for i in range(3)] for _ in range(3)]
print(_list2) # [[1,4,9], [1,4,9],[1,4,9]]

#1~10을 담는 리스트를 만들어 봅시다.
_list3 = [i for i in range(1,11)]
print(_list3)

#2,4,6,...,20을 담는 리스트를 만들어봅시다.
_list4 = [i for i in range(1,21) if i % 2 == 0]
print(_list4)

#주어진 리스트를 받아 3의 배수만 담는 리스트를 만들어봅시다.
tmp = [random.randrange(1,200) for i in range(100)]
_list5 = [i for i in tmp if i % 3 == 0]
print(_list5)

#값이 두개 들어있는 튜플을 받아 리스트를 생성하되, 튜플 내부의 값을 뒤집어 저장하세요.
list_of_tuple = [(i,j) for i in range(100) for j in range(100,0,-1)]
_list6 = [(j,i) for i,j in list_of_tuple]
print(_list6)

#주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 바꿔서 저장합시다.
_list7 = [15 if i > 15 else i for i in tmp]
print(_list7)

#두 개의 리스트를 합치되, 가능한 모든 조합을 저장하는 리스트를 만들어봅시다.
x = [i for i in range(5)]
y = [j for j in range(5)]
new_list = [(i,j) for i in x for j in y]
print(new_list)