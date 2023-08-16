import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #처음에 값을 다 담는다.
        load = collections.defaultdict(list)
        #결과
        result = -1

        for i in times:
            load[i[0]].append([i[2],i[1]])

        # k -> i 로 가는 것을 하나씩 찾아나가면서, 죄댓값을 갱신한다.
        # 그러다가 값이 없으면 -1을 return 시켜준다.
        for i in range(1,n+1):
            if i==k:
                continue

            he = []
            for j in load[k]:
                heapq.heappush(he,j)

            load_check = []
            for j in range(0,n+1):
                load_check.append([False]*(n+1))

            check = False

            while he :
                x,y = heapq.heappop(he)
                if y==i:
                    result = max(result, x)
                    check = True
                    break
                for j in load[y]:
                    if not load_check[y][j[1]] :
                        load_check[y][j[1]] = True
                        load_check[j[1]][y] = True
                        heapq.heappush(he,[j[0]+x,j[1]])
            if not check:
                return -1

        return result

print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))

