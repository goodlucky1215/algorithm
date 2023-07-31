import heapq
#다익스트라는 무조건 최소부터 찾아서 처리해야한다.
def dijkstra(distance,adj) :
    he = []
    heapq.heappush(he,[0,1])
    while he :
        d, x = heapq.heappop(he)
        for i in adj[x] :
            if d+i[0] < distance[i[1]] :
                distance[i[1]] = d+i[0]
                heapq.heappush(he,[distance[i[1]] ,i[1]])

def solution(N, road, K):
    distance = [float('inf')]*(N+1)
    distance[1] = 0
    adj = [[] for i in range(N+1)]
    for r in road :
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    dijkstra(distance,adj)
    answer = 0
    for i in distance :
        if i<=K : answer+=1 
    return answer