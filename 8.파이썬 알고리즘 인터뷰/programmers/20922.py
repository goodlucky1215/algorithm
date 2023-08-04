import sys
input = sys.stdin.readline
n, m = map(int,input().split())
a = list(map(int,input().split()))
answer = 0
result = 0
maps = {}
index = 0
for i in a:
    if i not in maps:
        maps[i]=0
    while maps[i]+1>m:
        maps[a[index]]-=1
        answer-=1
        index+=1
    maps[i]+=1
    answer+=1
    result = max(result,answer)
print(result)