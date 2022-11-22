import sys
input = sys.stdin.readline

t = int(input())

n = int(input())
arr_n = sorted(list(map(int, input().split())))

m = int(input())
arr_m = sorted(list(map(int, input().split())))

start = 0
end = max(arr_n);
mid = (start + end) // 2
