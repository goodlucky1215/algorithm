N,M=map(int,input().split()) #N이 끊어진 줄/M은 상점 수
G=[] #가게 6개가격 1개가격
m1 = 100000
m2 = 100000
for i in range(M):
    G = list(map(int, input().split()))
    m1 = min(m1, G[0]) # 패키지 최소값
    m2 = min(m2, G[1]) # 낱개 최소값

if m1>m2*6:
    print(m2*N)
elif m1>m2*(N%6):
    print(m1*(N//6)+m2*(N%6))
elif N%6>0:
    print(m1*(N//6+1))
else:
    print(m1*(N//6))
