N,C=map(int,input().split())
M=int(input())
max_box=[C]*(N-1)
truck=[]
result=0
for i in range(M):
    start,end,box=map(int,input().split())
    truck.append([])
    truck[i].append(end)
    truck[i].append(start)
    truck[i].append(box)
truck.sort()

for i in range(M):
    gap=truck[i][0]-truck[i][1]
    min_box=min(max_box[truck[i][1]-1:truck[i][0]-1])
    if min_box>truck[i][2]:
        for k in range(truck[i][1]-1,truck[i][0]-1):
            max_box[k]-=truck[i][2]
        result+=truck[i][2]
    else:
        for k in range(truck[i][1]-1,truck[i][0]-1):
            max_box[k]-=min_box
        result+=min_box
print(result)

