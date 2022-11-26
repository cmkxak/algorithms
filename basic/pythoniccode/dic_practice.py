#dic 기초
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = {}

for i in range(len(price)):
    _dict[fruit[i]] = price[i] # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}
print(_dict)

