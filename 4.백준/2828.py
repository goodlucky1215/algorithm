s,b=map(int,input().split())
j=int(input())
start=1
end=b
result=0
for i in range(j):
    apple=int(input())
    if end<apple:
        result+=(apple-end)
        start+=(apple-end)
        end+=(apple-end)
    elif apple<start:
        result+=(start-apple)
        end-=(start-apple)
        start-=(start-apple)
        
print(result)
