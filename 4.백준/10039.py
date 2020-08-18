import sys
d=0
for i in range(5):
    i=int(input())
    if 40>i:
        d+=40
    else:
        d+=i
print(d//5)
