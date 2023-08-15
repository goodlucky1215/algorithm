import collections
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #처음에 값을 다 담는다.
        load = collections.defaultdict(list)
        for i in times:
            load[i[0]].append([i[2],i[1]])
            load[i[1]].append([i[2],i[0]])

        #작은 값부터 정렬한다.
        for i in list(load):
            load[i].sort()

        #체크
        result = -1

        # k -> i 로 가는 것을 하나씩 찾아나가면서, 죄댓값을 갱신한다.
        # 그러다가 값이 없으면 -1을 return 시켜준다.
        for i in range(1,n+1):
            if i==k:
                continue
            deq = collections.deque()
            deq.append(load[k][0])
            load_all = 0
            while deq :
                x,y = deq.popleft()
                if y==i:
                    result = max(result, load_all+x)
                    break



        return 1

Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2)

