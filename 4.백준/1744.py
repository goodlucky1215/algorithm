n=int(input())
a=[]#음수 담는 통
b=[]#양수 담는 통
c=False#0이 있다면 True로바꿈 --> 왜냐면 그래야 음수가 홀수개일때 마지막 홀수는 0으로 바꿔줄수 있음
re=0
for i in range(n):
    y=int(input())
    if y<0:
        a.append(y)
    elif y==1:
        re+=1#1은 곱하는것보다 더해야 값이 더 크게 나올 수 있음
    elif y>0:
        b.append(y)
    else:
        c=True#0이있다면 True로 바꿔줌
a.sort()
b.sort()
if len(a)%2==0:
    for i in range(0,len(a),2):
        re+=a[i]*a[i+1]
else:#음수가 홀수개 일때
    for i in range(0,len(a)-1,2):
        re+=a[i]*a[i+1]
    if not c:#만약 0이 존재하지 않는다면 마지막음수는 -해주고 있다면 0과 곱해서 0으로 바꿔주므로 음수를 더 할 필요가 없
        re+=a[len(a)-1]
if len(b)%2==0:
    for i in range(0,len(b),2):
        re+=b[i]*b[i+1]
else:
    for i in range(1,len(b),2):
        re+=b[i]*b[i+1]
    re+=b[0]
print(re)
