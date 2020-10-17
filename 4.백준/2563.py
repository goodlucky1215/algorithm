n=int(input())
a=[]
s1,s2=10^9,10^9
s3,s4=0,0
for i in range(n):
    x,y=map(int,input().split())
    a.append([x,y])
    s1,s2=min(s1,x),min(s2,y)
    s3,s4=max(s3,x+10),max(s4,y+10)
box=[]
for i in range(s4):
    box.append([])
    box[i]=[0]*s3
for i in range(n):
    for j in range(10):
        box[j+a[i][1]][a[i][0]:a[i][0]+10]=[1]*10
re=0
for i in box:
    re+=sum(i)
print(re)
