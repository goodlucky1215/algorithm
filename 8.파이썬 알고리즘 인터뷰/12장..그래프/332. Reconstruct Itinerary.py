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

print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
