N,S,R=map(int,input().split())
Su=list(map(int,input().split()))
Su.sort(reverse=True)
Ru=list(map(int,input().split()))
Ru.sort(reverse=True)
for i in Ru:
    if i in Su:
        Su.remove(i)
    elif i+1 in Su:
        Su.remove(i+1)
    elif i-1 in Su:
        Su.remove(i-1)
print(len(Su))
