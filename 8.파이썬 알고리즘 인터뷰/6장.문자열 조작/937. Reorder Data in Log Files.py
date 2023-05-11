from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        string_list = []
        num_list = []
        for i in logs:
            if(i.index(0)[-1]>='0' and i.index(0)[-1]<='9') : num_list.append(i)
            else : string_list.append(i)
        string_list.sort(key = lambda x : (x.split()[1:],x.split()[:1]))
        return string_list+num_list


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        string_list = []
        num_list = []
        for i in logs:
            if i.split()[1].isdigit() : num_list.append(i)
            else : string_list.append(i)
        string_list.sort(key = lambda x : (x.split()[1:],x.split()[:1]))
        return string_list+num_list