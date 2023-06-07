import sys
input = sys.stdin.readline
n=int(input())
files = []
name_dict = {}
for i in range(n):
    files.append(input().rstrip())
for file in files:
    names = file.split('.')
    name_dict[names[1]] = name_dict.get(names[1], 0) + 1

name_keys = sorted(name_dict.keys())

for key in name_keys:
    print(key, name_dict[key])