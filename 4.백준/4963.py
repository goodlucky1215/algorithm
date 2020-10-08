import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(y, x, count):
    q = [[y, x]]
    while q:
        now = q.pop(0)
        for i in range(8):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if 0 <= nx < w and 0 <= ny < h and mat[ny][nx] == 1:
                mat[ny][nx] = count
                q.append([ny, nx])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mat = []
    for i in range(h):
        mat.append(list(map(int, input().split())))
    count = 2
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1:
                count += 1
                bfs(i, j, count)
    print(count - 2)

