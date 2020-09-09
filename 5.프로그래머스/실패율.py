def solution(N, stages):
    stages.sort()
    c={}
    for i in range(1,N+1):
        c[i]=0
    for i in range(1,N+1):
        a=0
        for j in stages:
            if i==j:
                a+=1
        b=len(stages)
        if a!=0:
            c[i]+=a/b
        del stages[0:a]
    result=sorted(c.items(),key=lambda x:x[1],reverse=True)
    d=[]
    for i,j in result:
        d.append(i)
    return  d

def solution(N, stages):
    stages.sort() #낮은 스테이지부터 정렬
    a={}#각각의 스테이지,실패율(key,value)
    for i in range(1,N+1): #각각의 스테이지
        a[i]=0#각 스테이지 값 처음엔 0
        for j in stages:
            if j==i:#만약 스테이지와 같은 값을 갖는 stages라면,
                a[i]+=1 #+1 (즉 스테이지에서 실패한 횟수)
            else:#sort로 이미 정렬했기 때문에 값이 다르다면 그 후는 다 다름.
                break #그래서 break
        k=a[i]#실패한 횟수 담음
        if k!=0:#만약 0이아니라면 -->0 일시 나누기에서 컴파일에러가 남
            a[i]/=len(stages)#i스테이지에따른, 실패한 횟수 스테이지를 전체스테이지에 나눠줌.
            stages=stages[k:]#다음 스테이지에서는 i스테이지까지 계산한 스테이지는 빼줘야하므로 [k:]부터 해줌.
    answer = sorted(a,key=lambda x:a[x],reverse=True) #실패율을 내림차순으로 정렬해서 key값만 담기.
    return answer
