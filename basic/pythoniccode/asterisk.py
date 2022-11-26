# * : 가변 인자로 활용한 예제
list = [1,2,3,4,5]
first_idx, *rest, last_idx = list
print(rest) #2 3 4

# * : Unpacking으로 활용한 예제
list2= [1,2,3,4,5]
print(*list2) #1 2 3 4 5

# Packing 예제
a,b,c = [1,2,3]
d = a,b,c
print(d)