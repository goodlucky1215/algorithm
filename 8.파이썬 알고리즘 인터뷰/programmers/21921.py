import sys

input = sys.stdin.readline
x, n = map(int, input().split())
d = list(map(int, input().split()))
result = [sum(d[:n]), 1]  # 처음 최대 방문자 수
num = result[0]
index = 0  # 앞에서부터 제거
for i in d[n:]:
    result1 = num - d[index] + i
    num = result1
    index += 1
    if result[0] < result1:
        result = [result1, 1]
    elif result[0] == result1:
        result[1] += 1

if result[0] == 0:
    print("SAD")
else:
    for i in result:
        print(i)