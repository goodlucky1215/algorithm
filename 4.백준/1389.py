n,m=map(int,input().split()) #사람수랑 1단계 관계수
per=[]
for i in range(n):
    per.append([])
    per[i]=[10**9]*n#일단 최악의 단계로 둠
for i in range(m):
    a,b=map(int,input().split())
    per[a-1][b-1]=1#a-1사람과 b-1사람의 관계는 1단계므로 바꿔줌
    per[b-1][a-1]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:#자기자신은 0단계
                per[i][j]=0
            else:#i사람과 j사람의 직접적으로의 관계 단계와 다른 사람을 통해서 알게된 단계수 중 작은 단계로 교체
                per[i][j]=min(per[i][j],per[i][k]+per[j][k])
#첫 번째 사람
p=sum(per[0])
re=0
for i in range(1,n):
    if p>sum(per[i]):
        p=sum(per[i])#나중에 사람의 단계가 더 좋다면 바꿔줌
        re=i
print(re+1)#결과출
