import sys
input = sys.stdin.readline
n = int(input())
p = []
for i in range(n):
    p.append(list(input().strip()))
answer = 0
candy = [[0,0],[1,0],[-1,0],[0,-1],[0,1]]
for i in range(n):
    for j in range(n):
        for c in candy:
            x = i+c[0]
            y = j+c[1]
            if 0<=x<n and 0<=y<n:
                p[i][j],p[x][y]=p[x][y],p[i][j]
                #행
                result1 = 1
                first = p[i][j]
                for y1 in range(j-1,-1,-1):
                    if p[i][y1]!=first:
                        break
                    result1+=1
                for y1 in range(j+1,n):
                    if p[i][y1]!=first:
                        break
                    result1+=1
                #열
                result2 = 1
                for x1 in range(i-1,-1,-1):
                    if p[x1][j]!=first:
                        break
                    result2+=1
                for x1 in range(i+1,n):
                    if p[x1][j]!=first:
                        break
                    result2+=1
                answer = max(answer,result1,result2)
                p[i][j], p[x][y] = p[x][y], p[i][j]
print(answer)
