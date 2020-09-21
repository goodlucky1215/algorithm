def find(su,a):
    p=0
    for i in su:
        p+=a[i[0]][i[1]]+a[i[1]][i[0]]#팀의 능력치를 모두 더해서
    return p#값 출력

from itertools import combinations 
n=int(input())#팀 수
team=list(range(n))#모든 팀 번호 리스트
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))#팀 들의 능력치 입력
b=list(combinations(team,n//2))#팀이 나뉘어지는 모든 경우의 수
z=[]
#콤비네이션은 맨 앞과 맨 뒤의 순서대로 없는 번호끼리 뭉쳐있기 때문에
#그래서 서로 다른 번호끼리 리스트 묶을 수 있음
for i in range(len(b)//2):
    su1=list(combinations(b[i],2))#그래서 i끼리의 모든 능력치를 가질 수 있는 인덱스 리스트
    su2=list(combinations(b[-i-1],2))#마찬가지고 끝에서부터 -i-1의 모든 능력치를 가질 수 있는 인덱스 리스트
    z.append(abs(find(su1,a)-find(su2,a)))#각각의 인덱스에 따른 능력치 팀 능력 계산
print(min(z))#최소값 출
