#민호가 모든 쌍의 도시를 최소이동시간으로 구해놨으므로,
#거쳐가는게 만약 더 짧다면 -1 로 출력
import sys
N=int(input())
a=[]
result=0
b=[]
for _ in range(N):
    a.append([])
    b.append([])
    print(a)
    for i in list(map(int,input().split())):
        a[-1].append(i)
        b[-1].append(i)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and k != j and k != i:
                if a[i][j]==a[i][k]+a[k][j]:
                    b[i][j]=0
                elif a[i][j]>a[i][k]+a[k][j]:
                    print(-1)
                    sys.exit()

for i in b:
    result+=sum(i)
print(result//2)
