n=int(input()) #입력값
a,b=0,1 #출력한 a갯수,b갯수
for i in range(1,n): 
    c=a+b 
    a=b #규칙에의하면 a는 b의 갯수가 되고,
    b=c #b는 a+b의 갯수가 됨.(a갯수가 b가 되므로 값이 달라져서 미리 c=a+b를 먼저 계산해줌) 
print(a,b) #출
