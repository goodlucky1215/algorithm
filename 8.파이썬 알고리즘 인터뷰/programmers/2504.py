import sys
input = sys.stdin.readline
def result():
    s = input().strip()
    sta = []
    for i in s:
        if i=="(" or i=="[":
            sta.append(i)
            continue
        elif i==")":
            if not sta or sta[-1]=="[":
                return 0
            if sta[-1]=="(":
                sta[-1]=2
            elif len(sta)==1:
                return 0
            else:
                first = sta.pop()
                if sta[-1]=="(":
                    sta[-1] = first*2
                else:
                    return 0
        elif i=="]":
            if not sta or sta[-1]=="(":
                return 0
            if sta[-1]=="[":
                sta[-1]=3
            elif len(sta)==1:
                return 0
            else:
                first = sta.pop()
                if sta[-1]=="[":
                    sta[-1] = first*3
                else:
                    return 0
        if len(sta)>1 and sta[-1]!="(" and sta[-1]!="[" and sta[-2]!="(" and sta[-2]!="[":
            first = sta.pop()
            sta[-1]+=first
    if len(sta)==1 and sta[0]!="(" and sta[0]!="[" and sta[0]!="(" and sta[0]!="[":
        return sta[0]
    else:
        return 0
print(result())
