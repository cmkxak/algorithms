s=int(input())
tmp=0
sum=0
while True:
    if sum + tmp < s:
        tmp+=1
        sum+=tmp
    else:
        break
print(tmp)