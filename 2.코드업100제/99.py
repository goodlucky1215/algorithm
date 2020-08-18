m=[]
for i in range(10):
    m.append([])
    for j in range(10):
        m[i].append(0)

for i in range(10):
    for j in range(10):
        m[i][0]=1
        m[i][9]=1
        m[0][i]=1
        m[9][i]=1

m[1][3]=1
m[2][3]=1
m[2][4]=1
m[2][5]=1
m[3][7]=1
m[4][7]=1
m[5][7]=1
m[6][7]=1
m[5][5]=1
m[6][5]=1
m[7][5]=1
m[6][6]=2

for i in range(10):
    for j in range(10):
        print(m[i][j], end=' ')
    print(" ")


x = 1
y = 1
    
while m[6][6]==2:
    if m[x][y] !=1:
        m[x][y]= 9
        y+=1
    else:
        x+=1
        m[x][y-1]= 9

print(" ")

for i in range(10):
    for j in range(10):
        print(m[i][j], end=' ')
    print(" ")


        
    
