from typing import List
import sys
input = sys.stdin.readline

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_sort = sorted(tickets)
        tickets_fisrt = 0
        l = len(tickets)
        tickets_len = l+1
        check = [False]*l
        result = ['JFK']

        #첫번째 길 찾음
        def first_ticket(tickets_fisrt):
            for i in range(tickets_fisrt,l):
                if tickets_sort[i][0]=='JFK':
                    check[i]=True
                    result.append(tickets_sort[i][1])
                    return i

        def dfs():
            if tickets_len == len(result):
                return

            for i in range(l):
                if check[i]==False and tickets_sort[i][0]==result[-1]:
                    check[i]=True
                    result.append(tickets_sort[i][1])
                    dfs()
                    if tickets_len == len(result):
                        return
                    check[i]=False
                    result.pop()

        while tickets_len != len(result):
            tickets_fisrt = first_ticket(tickets_fisrt)
            dfs()
            if tickets_len == len(result):
                break
            check[tickets_fisrt] = False
            result.pop()
            tickets_fisrt+=1

        return result


    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        result = []
        for a, b in sorted(tickets,reverse=True):
            if a not in graph:
                graph[a]=[]
            graph[a].append(b)

        def dfs(a : str):
            while a in graph and graph[a]:
                dfs(graph[a].pop())
            result.append(a)

        dfs('JFK')

        return result[::-1]

print(Solution().findItinerary1([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
