n = input()
left_sum=0
right_sum=0
divide_len = len(n)//2

for i in n[:divide_len]:
    left_sum+=int(i)
for i in n[divide_len:]:
    right_sum+=int(i)
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")