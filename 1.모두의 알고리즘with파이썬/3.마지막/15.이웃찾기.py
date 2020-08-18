def all_friend(g,start):
    friend=[start]
    fr=[start]
    print(start)
    while friend:
        p=friend.pop(0) 
        for j in g[p]:
            if j not in fr:
                print(j)
                friend.append(j)
                fr.append(j)
    return


        
fr_info = {
    'summer':['john','justin','mike'],
    'john':['summer','justin'],
    'justin';:['john','summer','mike','may'],
    'mike':['summer','justin'],
    'may':['justin','kim'],
    'kim':['may'],
    'tom':['jerry'],
    'jerry':['tom']
}

all_friend(fr_info,'summer')


#친밀한 정도까지 계산하기
def all_friend(g,start):
    st=[start]
    fr={start:0}
    j=0
    print(st[0],":",j)
    while st:
        q=st.pop(0)
        j = fr[q]+1
        for i in g[q]:
            if i not in fr:
                fr[i]=j
                print(i,":",j)
                st.append(i)
    return

all_friend(fr_info,'summer')

def number(g,start):
    qu=[]
    done={}
    qu.append((start,0))
    done.add(start)
    while qu:
        (p,d)=qu.pop(0)
        print(p,d)
        for x in g[p]:
            if x not in done:
                qu.append((x,d+1))
                done.add(x)
            
    
