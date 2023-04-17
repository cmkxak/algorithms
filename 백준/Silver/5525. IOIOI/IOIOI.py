#IOIOI
def make_sample(n):
    sample=''
    cnt1, cnt2 = 'I' * (n+1), 'O' * (n)
    for i in range(len(cnt1 + cnt2)):
        if i % 2 == 0:
            sample+='I'
        else:
            sample+='O'
    return sample

n=int(input())
s_len = int(input())
s= input()

sample = make_sample(n)
s_idx,e = 0, len(sample)
answer=0
while e <= len(s):
    if s[s_idx:e] == sample:
        answer+=1
        s_idx+=1
        e+=1
    else:
        s_idx+=1
        e+=1
print(answer)