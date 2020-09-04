n,k=map(int,input().split()) #물건 수와 한계인 무게
a=[[0]*(k+1) for _ in range(n+1)] #각각의 물건이 들어올 때마다 비교할 통
for i in range(1,n+1):
    we,va=map(int,input().split()) #물건 입력 받음(무게, 가치)
    for j in range(1,k+1): #1부터 최대 무게 까지 for루프
            if j<we: #만약 무게가 j보다 큰 물건이라면
                a[i][j]=a[i-1][j] #j는 더 이상 비교할 수가 없으므로 전 무게를 입력
            else:#만약 무게가 j랑 같거나 크다면~~
                #만약 j=6 이고 we가 4라면 6-4=2므로
                #현재 we가 가지는 4무게를 가진 가치 va와 전에 가지고 있는 2무게를 가진 가치를 더한다
                #그러면 전에 가지고 있는 6무게와 비교해서 더 큰값을 가지게 만들면 된다.
                a[i][j]=max(a[i-1][j],a[i-1][j-we]+va)
#맨 마지막 줄에서 가장 큰 가치를 가진 값을 뽑
print(max(a[n]))
