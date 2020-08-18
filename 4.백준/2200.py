n=int(input())
s=list(map(int, input().split()))
#최고차항은 '='까지 갯수를 포함해서 n*2개씩 필요(무조건 계수가 1)
result=n*2
for i in s[1:]:
    #다른 차항은 2개씩 늘어나고 숫자 자리수 3이면 +4,자릿수가 4면 +5 이런씩으로
    if i>0:
        result+=(len(str(i))+1)
print(result)
