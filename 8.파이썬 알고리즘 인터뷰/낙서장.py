import collections
import queue

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

