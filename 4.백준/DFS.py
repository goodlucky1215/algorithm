graph=dict()
graph['A']=['B','C']
graph['B']=['A','D']
graph['C']=['A','G','H','I']
graph['D']=['B','E','F']
graph['E']=['D']
graph['F']=['D']
graph['G']=['C']
graph['H']=['C']
graph['I']=['C','J']
graph['J']=['I']

graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A', 'D', 'F']),
         'C': set(['A', 'G']),
         'D': set(['B']),
         'E': set(['A', 'F']),
         'F': set(['B', 'E']),
         'G': set(['G'])}

def dfs(graph, root):
  visited = [] # 각 꼭짓점(vertex)이 방문되었는지 기록
  stack = [root, ]
 
  while stack: # stack 이 비게 되면 탐색 끝
    vertex = stack.pop() # 방문되어지고 있는 꼭짓점
    if vertex not in visited: #
      visited.add(vertex)
      stack.extend(graph[vertex] - visited)
 
  return visited;


print(dfs(graph, 'A'))

def dfs(graph,start_node):
    visited,need_visit=list(),list()
    need_visit.append(start_node)

    while need_visit:
        node=need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited
        
        
print(dfs(graph,'A'))


