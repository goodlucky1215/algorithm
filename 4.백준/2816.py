N=int(input()) #채널의 수
a=[] #채널을 담을 통
result=''#출력값
for i in range(N): 
    a.append(input()) #채널 이름
    if a[i]=='KBS1': #처음에 찾을 KBS1의 인덱스 번호를 저장
        k=i
def find(k,b): #find(찾을 인덱스 번호,채널을 넣을 번호 자리)
    global result,a #밖에 있는 값 불러오기
    result+='1'*k #내가 찾는 채널의 번호까지 리모콘으로 내림.
    for i in range(k,b,-1): #찾는 채널의 번호에서 넣을 번호자리까지
        a[i],a[i-1]=a[i-1],a[i] #4번을 이용해서 바꿔 올릴 거임(찾는 채널으로 화살표를 가르키게 됨)
    result+='4'*(k-b) #내가 찾은 채널을 b번째 자리로 올린 4번의 횟수
find(k,0) #KBS1을 먼저 찾고
k=a.index('KBS2') #KBS2의 인덱스를 찾아서
find(k,1) #KBS2를 찾아주면 끝
print(result)
#4개의 채널리스트를 이용하지 않고 1,4만을 이용해서 문제를 간단하게 해결하는게 핵심.
#4번으로 바꾸면 내게 필요한 kbs1과 kbs2로 화살표가 채널을 가리키고 있어서 더 간단!



