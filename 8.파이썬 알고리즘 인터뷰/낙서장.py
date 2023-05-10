import collections
import queue
from typing import List


logs : List[str] = []
logs.append("aaa")
print(logs)
a = []
a.append(map('a','z'))
print(a['a'])
for i in logs : print(i[:1])
s= List[str]
b = []
print(type(s),type(b))
a = collections.deque();
a.append('a')
a.append('b')
a.append('c')
print(a)
a.pop()
print(a)

b = queue.Queue()
b.put('a')
b.put('b')
b.put('c')
print(b.queue)
b.get()
print(b.queue)

s = ["h2","e","l","l","o"]
print(len(s))
s[:] = s[::-1]
print("s의 주소 :",id(s))
s= s[::-1]
print("s의 주소 :",id(s))