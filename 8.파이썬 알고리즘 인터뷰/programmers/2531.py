n, d, k, c = map(int,input().split())
sushi = [0]*3001 #먹은 초밥 체크
result = 0 #먹은 스시 종류
qu = []
for i in range(n):
    su = int(input())
    qu.append(su)

# 처음 default
for i in range(-k,0):
    #초밥 종류 체크
    if sushi[qu[i]]==0:
        sushi[qu[i]]+=1
        result+=1
    else:
        sushi[qu[i]]+=1
check=-k
answer = result

for i in range(n):
    #초밥 종류 체크
    if sushi[qu[i]]==0:
        sushi[qu[i]]+=1
        result+=1
    else:
        sushi[qu[i]]+=1

    #초밥 갯수 체크
    sushi[qu[check]]-=1
    if sushi[qu[check]]==0:
        result-=1
    #초밥 종류 체크
    answer = max(result+1 if sushi[c]==0 else result,answer)
    check+=1

print(answer)
