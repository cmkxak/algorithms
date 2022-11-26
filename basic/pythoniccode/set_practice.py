#중복된 값이 제거된 리스트 만들기
_list = [4, 1, 5, 1, 5, 6, 4, 3, 1, 38, 12, 42, 88, 99, 88]
_list = list(set(_list))
print(_list)

#lambda를 활용해보자.
test_list = ['test', 'TEst', 'ttttessst','tesT']
converted_list = [set(map(lambda string: string.lower(), test_list))]
print(converted_list)