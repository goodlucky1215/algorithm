from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        string_list = List[str]
        num_list = List[str]
        logs.index(0)
        for i in logs:
            if(i.index(0)[-1]>='0' and i.index(0)[-1]<='9') : num_list.append(i)
            else : string_list.append(i)