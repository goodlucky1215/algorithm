def all_friends(g, start):
    qu=[]
    done=set()
    qu.append(start)
    done.add(start)
    
    while qu:
        q=qu.pop(0)
        print(q)
        for x in g[q]:
            if x not in done:
                qu.append(x)
                done.add(x)


def all_friends2(g, start):
    qu=[]
    done=set()
    qu.append((start,0))
    done.add(start)

    while qu:
        (q, d)=qu.pop(0)
        print(q,d)
        for x in g[q]:
            if x not in done:
                qu.append((x,d+1))
                done.add(x)
                


friend={
    'tom':['jerry','kein'],
    'kein':['tom'],
    'jerry':['tom','jinny','buta'],
    'jinny':['jerry'],
    'buta':['jerry']
    }

all_friends(friend,'tom')
all_friends2(friend,'tom')
