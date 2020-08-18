def find_same_name(a):
    dic={}
    result=[]
    for i in a:
        if i not in dic:
            dic[i]=1
        elif i in dic:
            result.append(i)
    return result

n=["tom","jerry","mike","tom","mike"]
print(find_same_name(n))

def find_same_name(a,b):
    if b in a:
        return a[b]
    return "?"

n={
    1:"tom",
    32:"jerry",
    64:"mike",
    105:"tommy"
    }
print(find_same_name(n,64))
print(find_same_name(n,23))
