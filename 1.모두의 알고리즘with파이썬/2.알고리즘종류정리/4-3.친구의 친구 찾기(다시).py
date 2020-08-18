#내 친구의 친구이면 모두 출력하는 모든 친구를 찾는 알고리즘
def all_friends(g,start):
    qu = []
    done =set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)


fr_info = {
    'summer':['john','justin','mike'],
    'john':['summer','justin'],
    'justin':['john','summer','mike','may'],
    'mike':['summer','justin'],
    'may':['justin','kim'],
    'kim':['may'],
    'tom':['jerry'],
    'jerry':['tom']
}
all_friends(fr_info,'summer')
print('')
all_friends(fr_info,'jerry')
print('')

#모든 친구를 찾아서 친밀도를 계산하는 알고리즘
def all_friends(g,start):
    qu=[]
    done=set()

    qu.append((start,0))
    done.add(start)

    while qu:
        (p, d) = qu.pop(0)
        print(p,d)
        for x in g[p]:
            if x not in done:
                qu.append((x,d+1))
                done.add(x)
        

all_friends(fr_info,'summer')
print('')
all_friends(fr_info,'jerry')
print('')

#예제
def all_friend(g,start):
    qu=[]
    done=set()

    qu.append(start)
    done.add(start)

    while qu:
        p=qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

a = {
    1:[2,3],
    2:[1,4,5],
    3:[1],
    4:[2],
    5:[2]
    }
all_friend(a,1)
