maze={
    'a':['e'],
    'b':['c','f'],
    'c':['b','d'],
    'd':['c'],
    'e':['a','i'],
    'f':['b','g','j'],
    'g':['f','h'],
    'h':['g','l'],
    'i':['e','m'],
    'j':['f','k','n'],
    'k':['j','o'],
    'l':['h','p'],
    'm':['i','n'],
    'n':['m','j'],
    'o':['k'],
    'p':['l']
    }

def solve_maze(a,start,end):
    qu=[]
    done=set()
    qu.append(start)
    done.add(start)
    
    while qu:
        q = qu.pop(0)
        v = q[-1] #q가 qu.append(q+x)로 통채로 담기때문에 나중엔 문장이 되기 때문에 q[-1]로 담아야한다.
       #print(q)
        if v==end:
            return q
        for x in a[v]:
            if x not in done:
                qu.append(q+x)
                done.add(x)
    return "?"
            
print(solve_maze(maze,'a','p'))
