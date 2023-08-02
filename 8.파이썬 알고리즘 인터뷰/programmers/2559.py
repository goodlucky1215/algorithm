n, k = map(int,input().split())
s = list(map(int, input().split()))

result = sum(s[:k])
before = sum(s[:k])
for i in range(1,n-k+1):
    before = before-s[i-1]+s[i+k-1]
    result = max(before, result)
print(result)